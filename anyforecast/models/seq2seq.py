from typing import Literal

from anyforecast.definitions import get_project_path
from anyforecast.estimator import MLFlowEstimator


class Seq2Seq(MLFlowEstimator):
    """Handles end-to-end training and deployment of Seq2Seq model.

    Parameters
    ----------

    max_epochs : int, default=10
        The number of epochs to train for each :meth:`fit` call. Note that you
        may keyboard-interrupt training at any time.

    verbose : int, default=1
        This parameter controls how much print output is generated by
        the net and its callbacks. By setting this value to 0, e.g. the
        summary scores at the end of each epoch are no longer printed.

    experiment_name : str, default=None
        Name of experiment under which to launch the run.

    experiment_id : str, default=None
        ID of experiment under which to launch the run.

    run_name : str, default=None
        The name to give the MLflow Run associated with the project execution.
        If None, the MLflow Run name is left unset.

    env_manager : str, default=None
        Specify an environment manager to create a new environment for the run
        and install project dependencies within that environment. If
        unspecified, MLflow automatically determines the environment manager to
        use by inspecting files in the project directory.
    """

    def __init__(
        self,
        train: str,
        group_ids: str,
        timestamp: str,
        target: str,
        time_varying_known: str | None = None,
        time_varying_unknown: str | None = None,
        static_categoricals: str | None = None,
        static_reals: str | None = None,
        max_prediction_length: int = 6,
        max_encoder_length: int = 24,
        freq: str = "D",
        device: str = "cpu",
        max_epochs: int = 10,
        verbose: int = 1,
        experiment_name: str | None = None,
        experiment_id: str | None = None,
        run_name: str | None = None,
        env_manager: Literal["local", "virtualenv", "conda"] | None = None,
    ):
        self.train = train
        self.group_ids = group_ids
        self.timestamp = timestamp
        self.target = target
        self.time_varying_known = time_varying_known
        self.time_varying_unknown = time_varying_unknown
        self.static_categoricals = static_categoricals
        self.static_reals = static_reals
        self.max_prediction_length = max_prediction_length
        self.max_encoder_length = max_encoder_length
        self.freq = freq
        self.device = device
        self.max_epochs = max_epochs
        self.verbose = verbose

        project_uri = get_project_path("skorchforecasting")
        entry_point = "train_seq2seq"

        super().__init__(
            project_uri=project_uri,
            entry_point=entry_point,
            experiment_name=experiment_name,
            experiment_id=experiment_id,
            run_name=run_name,
            env_manager=env_manager,
        )

    def get_parameters(self) -> dict:
        return {
            "train": self.train,
            "group-ids": self.group_ids,
            "timestamp": self.timestamp,
            "target": self.target,
            "time-varying-known": self.time_varying_known,
            "time-varying-unknown": self.time_varying_unknown,
            "static-categoricals": self.static_categoricals,
            "static-reals": self.static_reals,
            "max-prediction-length": self.max_prediction_length,
            "max-encoder-length": self.max_encoder_length,
            "freq": self.freq,
            "device": self.device,
            "max-epochs": self.max_epochs,
            "verbose": self.verbose,
        }
