import pyarrow as pa
from stonewave.sql.udtfs.logger import logger


class RecordBatchBuilder(object):
    def __init__(self):
        self.columns = {}
        self.schema = {}
        self._row_count = 0

    def column_names(self):
        return self.schema.keys()

    def add_column(self, column_name, data_type):
        """
        Append a column to the builder. If the column with the same name exists in the builder, it will NOT be added again.
        :param column_name: the name of the column
        :param data_type: pyarrow's field data type, for example, pyarrow::utf8()
        :return: None
        """
        if column_name not in self.columns:
            self.columns[column_name] = []
            self.schema[column_name] = data_type

    def append(self, column, value):
        """
        Append a new value for a given column.
        After appending values for all columns in a row,
        caller needs to call `increase_row_count` to ensure the builder's row_count is increased correctly.
        :param column: the name of the column
        :param value: the new value to be append to the column
        :return:
        """
        self._fill_null_for_all_builders(self._row_count)
        return self.columns.get(column).append(value)

    def extend(self, column, values):
        """
        Append multiple new values for a new given column.
        After appending values for all columns in a row,
        caller needs to call `increase_row_count` to ensure the builder's row_count is increased correctly.
        :param column: the name of the column
        :param values: a list of new values to be appended to the columns
        :return:
        """
        # caller needs to call `increase_row_count` to ensure the builder's row_count is increased correctly
        self._fill_null_for_all_builders(self._row_count)
        return self.columns.get(column).extend(values)

    def num_fields(self):
        """
        :return: the number of fields (columns) currently in this builder
        """
        return len(self.schema)

    def flush(self):
        """
        Flush the contents in the record build to build a record batch.
        return the record batch built from the contents in the builder,
        and return None if the built record batch is empty.
        """
        if self.columns:
            logger.debug(
                "flushing contents from record batch builder",
                columns=len(self.columns),
                row_count=self._row_count,
            )
            self._fill_null_for_all_builders(self._row_count)
            arrow_arrays = [pa.array(array, self.schema[col]) for col, array in self.columns.items()]
            batch = pa.RecordBatch.from_arrays(arrow_arrays, list(self.columns.keys()))
            # clear all arrays
            for col in self.columns.keys():
                self.columns[col] = []
            self._row_count = 0
            return batch
        # having null rows only, use empty batch to indicates this
        elif self._row_count > 0:
            self._row_count = 0
            batch = pa.RecordBatch.from_arrays([])
            return batch
        else:
            return None

    def row_count(self):
        """
        Return the number of rows in the builder
        :return:
        """
        return self._row_count

    def increase_row_count(self, increment=1):
        """
        Increase the number of rows in the builder. This is necessary after caller append values for individual column
        by calling `append` or `extend` API in this class.
        :param increment: the number of rows to be increased, by default, this method increases by 1
        :return:
        """
        self._row_count += increment

    def append_null_row(self):
        """
        append a null row to the builder.
        The row count will be automatically maintained.
        :return:
        """
        for array in self.columns.values():
            array.append(None)
        self.increase_row_count()

    def append_row(self, kv_pairs):
        """
        Append a row with as key value pairs, represented by a Python dictionary.
        The key represents the column name and the value represents the column value, which is pyarrow.utf8() type
        :param kv_pairs: the row's field names and values
        :return:
        """
        self._fill_null_for_all_builders(self._row_count)
        for key, value in kv_pairs.items():
            # TODO: we don't support creating multi value field yet in python
            self.add_column(key, pa.utf8())
            array = self._get_column_array(key)
            array.append(value)
        self.increase_row_count()

    def _fill_null_for_all_builders(self, new_row_count):
        for array in self.columns.values():
            null_count = new_row_count - len(array)
            for _ in range(0, null_count):
                array.append(None)

    def _get_column_array(self, column):
        return self.columns.get(column)
