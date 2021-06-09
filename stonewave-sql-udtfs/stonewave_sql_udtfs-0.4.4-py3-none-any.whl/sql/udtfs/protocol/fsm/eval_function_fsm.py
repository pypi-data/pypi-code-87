from transitions import Machine
from stonewave.sql.udtfs.protocol import ipc
from stonewave.sql.udtfs.constants import PROCESS_ERROR_MSG_TEMPLATE
from stonewave.sql.udtfs.table_row_writer import TableRowWriter


class EvalFunctionFsm(object):
    states = ["start", "wait_for_next", "end"]

    def __init__(self, func, batch_sender):
        self.func = func
        self._batch_sender = batch_sender
        self._row_writer = TableRowWriter()
        self._is_evaluated = False

        self.machine = Machine(model=self, states=EvalFunctionFsm.states, initial="start")

        self.machine.add_transition(
            trigger="eval",
            source="start",
            dest="wait_for_next",
            before="eval_params",
        )

        self.machine.add_transition(
            trigger="next",
            source="wait_for_next",
            dest="wait_for_next",
            after="send_next_batch",
        )

        self.machine.add_transition(trigger="end", source="*", dest="end", before="end_evaluation")

    def eval_params(self, params, respond):
        self.send_next_batch(params, respond)

    def send_next_batch(self, params, respond):
        if not self._is_evaluated:
            self.func.initialize(self._row_writer)
            try:
                func_name = self.func.get_name()
                self.func.process(self._row_writer, 0, params)
            except Exception as e:
                respond("end", PROCESS_ERROR_MSG_TEMPLATE.format(func_name, str(e)))
                return
            self._is_evaluated = True

        batch = self._row_writer.flush(True)
        if batch is not None:
            self._batch_sender.send(batch, respond)
            return
        else:
            self.end(params, respond)

    def end_evaluation(self, params, respond):
        respond("end")
