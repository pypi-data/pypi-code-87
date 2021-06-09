import esphome.codegen as cg
import esphome.config_validation as cv
from esphome import pins
from esphome.components import i2c
from esphome.const import CONF_ID, CONF_NUMBER, CONF_MODE, CONF_INVERTED

CONF_KEYPAD = "keypad"
CONF_KEY_ROWS = "key_rows"
CONF_KEY_COLUMNS = "key_columns"
CONF_SLEEP_TIME = "sleep_time"
CONF_SCAN_TIME = "scan_time"
CONF_DEBOUNCE_TIME = "debounce_time"

DEPENDENCIES = ["i2c"]
MULTI_CONF = True

sx1509_ns = cg.esphome_ns.namespace("sx1509")
SX1509GPIOMode = sx1509_ns.enum("SX1509GPIOMode")
SX1509_GPIO_MODES = {
    "INPUT": SX1509GPIOMode.SX1509_INPUT,
    "INPUT_PULLUP": SX1509GPIOMode.SX1509_INPUT_PULLUP,
    "OUTPUT": SX1509GPIOMode.SX1509_OUTPUT,
}

SX1509Component = sx1509_ns.class_("SX1509Component", cg.Component, i2c.I2CDevice)
SX1509GPIOPin = sx1509_ns.class_("SX1509GPIOPin", cg.GPIOPin)

KEYPAD_SCHEMA = cv.Schema(
    {
        cv.Required(CONF_KEY_ROWS): cv.int_range(min=1, max=8),
        cv.Required(CONF_KEY_COLUMNS): cv.int_range(min=1, max=8),
        cv.Optional(CONF_SLEEP_TIME): cv.int_range(min=128, max=8192),
        cv.Optional(CONF_SCAN_TIME): cv.int_range(min=1, max=128),
        cv.Optional(CONF_DEBOUNCE_TIME): cv.int_range(min=1, max=64),
    }
)

CONFIG_SCHEMA = (
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(SX1509Component),
            cv.Optional(CONF_KEYPAD): cv.Schema(KEYPAD_SCHEMA),
        }
    )
    .extend(cv.COMPONENT_SCHEMA)
    .extend(i2c.i2c_device_schema(0x3E))
)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await i2c.register_i2c_device(var, config)
    if CONF_KEYPAD in config:
        keypad = config[CONF_KEYPAD]
        cg.add(var.set_rows_cols(keypad[CONF_KEY_ROWS], keypad[CONF_KEY_COLUMNS]))
        if (
            CONF_SLEEP_TIME in keypad
            and CONF_SCAN_TIME in keypad
            and CONF_DEBOUNCE_TIME in keypad
        ):
            cg.add(var.set_sleep_time(keypad[CONF_SLEEP_TIME]))
            cg.add(var.set_scan_time(keypad[CONF_SCAN_TIME]))
            cg.add(var.set_debounce_time(keypad[CONF_DEBOUNCE_TIME]))


CONF_SX1509 = "sx1509"
CONF_SX1509_ID = "sx1509_id"

SX1509_OUTPUT_PIN_SCHEMA = cv.Schema(
    {
        cv.Required(CONF_SX1509): cv.use_id(SX1509Component),
        cv.Required(CONF_NUMBER): cv.int_,
        cv.Optional(CONF_MODE, default="OUTPUT"): cv.enum(
            SX1509_GPIO_MODES, upper=True
        ),
        cv.Optional(CONF_INVERTED, default=False): cv.boolean,
    }
)
SX1509_INPUT_PIN_SCHEMA = cv.Schema(
    {
        cv.Required(CONF_SX1509): cv.use_id(SX1509Component),
        cv.Required(CONF_NUMBER): cv.int_,
        cv.Optional(CONF_MODE, default="INPUT"): cv.enum(SX1509_GPIO_MODES, upper=True),
        cv.Optional(CONF_INVERTED, default=False): cv.boolean,
    }
)


@pins.PIN_SCHEMA_REGISTRY.register(
    CONF_SX1509, (SX1509_OUTPUT_PIN_SCHEMA, SX1509_INPUT_PIN_SCHEMA)
)
async def sx1509_pin_to_code(config):
    parent = await cg.get_variable(config[CONF_SX1509])
    return SX1509GPIOPin.new(
        parent, config[CONF_NUMBER], config[CONF_MODE], config[CONF_INVERTED]
    )
