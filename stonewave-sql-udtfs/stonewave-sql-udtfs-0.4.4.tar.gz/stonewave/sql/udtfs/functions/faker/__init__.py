from faker import Faker
import pyarrow as pa
from faker_web import WebProvider
from faker_vehicle import VehicleProvider
from faker_wifi_essid import WifiESSID as WifiEssidProvider
from faker_microservice import Provider as MicroServiceProvider
from faker_credit_score import CreditScore as CreditScoreProvider
import decimal
from stonewave.sql.udtfs.base_function import BaseFunction
from stonewave.sql.udtfs.logger import logger

fake = Faker()
fake.add_provider(WebProvider)
fake.add_provider(WifiEssidProvider)
fake.add_provider(MicroServiceProvider)
fake.add_provider(VehicleProvider)
fake.add_provider(CreditScoreProvider)


def _get_data_type(field_faker):
    if not field_faker:
        return pa.utf8()
    else:
        value = field_faker()
        # bool needs to be placed before int because isinstance(True, int) == True
        if isinstance(value, bool):
            return pa.bool_()
        elif isinstance(value, int):
            return pa.int64()
        elif isinstance(value, float):
            return pa.float64()
        # elif isinstance(value, decimal.Decimal):
        # return pa.decimal128(13)
        else:
            return pa.utf8()


class FakerFunction(BaseFunction):
    def __init__(self):
        pass

    def get_name(self):
        return "faker"

    def _safe_cast(self, value, to_type, default=None):
        try:
            return to_type(value)
        except (ValueError, TypeError):
            return default

    def process(self, row_writer, row_idx, args):
        row_count = max(0, self._safe_cast(args[0], int, 0))
        if args[1] is None:
            logger.debug("faker column name is not provided, no row is produced")
            return
        columns = [c.strip() for c in args[1].split(",")]
        non_duplicated_column_names = self._non_duplicated_column_names(columns)

        record_batch_builder = row_writer.record_batch_builder
        for fake_column_method, fake_column_name in zip(columns, non_duplicated_column_names):
            field_faker = getattr(fake, fake_column_method, None)
            field_type = _get_data_type(field_faker)

            record_batch_builder.add_column(fake_column_name, field_type)

            field_faker = getattr(fake, fake_column_method, None)
            array = [field_faker() if field_faker else None for i in range(row_count)]
            record_batch_builder.extend(fake_column_name, array)
        record_batch_builder.increase_row_count(row_count)
        logger.debug(
            "rows generated via faker",
            row_count=row_count,
            builder_row_count=record_batch_builder.row_count(),
        )

    def _non_duplicated_column_names(self, columns):
        column_set = set()
        non_duplicated_column_names = []
        for column in columns:
            column_id = 0
            non_duplicated_column_name = column
            if non_duplicated_column_name in column_set:
                column_id += 1
                non_duplicated_column_name = "{}${}".format(column, column_id)
            column_set.add(non_duplicated_column_name)
            non_duplicated_column_names.append(non_duplicated_column_name)
        return non_duplicated_column_names
