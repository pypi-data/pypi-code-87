from stonewave.sql.udtfs.base_function import BaseFunction
import pyarrow as pa


class SummarizeFunction(BaseFunction):
    def __init__(self):
        self.tables = []

    def get_name(self):
        return "summarize"

    def process(self, row_writer, row_idx, args):
        assert len(args) > 0
        batch = args[0]
        if batch is not None:
            table = pa.Table.from_batches([batch])
            # FIXME: the current implementation caches all batches, which is not necessary
            self.tables.append(table)
        else:
            self.summarize(row_writer)

    def summarize(self, row_writer):
        if self.tables:
            table = pa.concat_tables(self.tables, promote=True)
            df = table.to_pandas()
            desc_df = df.describe(datetime_is_numeric=True)
            # the df is transposed because it contains mixed type column, which is not allowed in arrow
            desc_df = desc_df.transpose()
            desc_df.insert(0, "fields", desc_df.index)
            desc_table = pa.Table.from_pandas(desc_df, preserve_index=False)
            batches = desc_table.to_batches()
            row_writer.batch_iterator = iter(batches)
        else:
            return
