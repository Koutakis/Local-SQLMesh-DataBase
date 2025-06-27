MODEL (
    name sqlmesh.sqlmesh.patients_summary,
    kind FULL,
    cron '@daily'
);

SELECT 
    identifier, 
    source, 
    valid_pin
FROM 
    sqlmesh.sqlmesh.test_patient_data