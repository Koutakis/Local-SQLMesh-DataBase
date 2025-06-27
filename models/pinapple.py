from sqlmesh import model
import requests
import pandas as pd
from sqlmesh.core.model.kind import ModelKindName
import typing as t
from datetime import datetime
from sqlmesh import ExecutionContext, model
 

@model(
    "SQLMESH.test_patient_data",
    kind=dict(
        name=ModelKindName.FULL
    ),
    columns={
        "identifier": "string",
        "source": "string",
        "comment": "string",      
        "added_by": "string",
        "valid_pin": "boolean",
        "last_modified": "string"  
    }
)
def execute(
    context: ExecutionContext,
    start: datetime,
    end: datetime,
    execution_time: datetime,
    **kwargs: t.Any,
) -> pd.DataFrame:    
    response = requests.get("https://testpatientlisa.apps.ocp.mta.karolinska.se/testpatient/retrieve")  # Replace with real URL
    data = response.json()

    patients = data.get("patients", [])
    df = pd.DataFrame(patients)
    return df
 