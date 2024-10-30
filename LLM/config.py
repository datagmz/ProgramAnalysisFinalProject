from dataclasses import dataclass

@dataclass(frozen=True)
class Config:
    AZURE_OPENAI_ENDPOINT: str
    AZURE_OPENAI_KEY: str
    AZURE_OPENAI_DEPLOYMENT_NAME: str

    def __post_init__(self):
        # Checks that all attributes are defined
        for attr in vars(self):
            if not getattr(self, attr):
                raise ValueError(f"{attr} is not defined in the config file")
        

