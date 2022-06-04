# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""

This is an example dag for ECSOperator.

The task "remote-sensing-Container-orchestration" runs a basic task in `hello-world` cluster.
It overrides the command in the `tf-test-write-s3-hello` container.

"""

import datetime
import os

from airflow import DAG
from airflow.providers.amazon.aws.operators.ecs import ECSOperator
from airflow.operators.python import PythonOperator
import boto3
import json
from airflow.models import Variable


DEFAULT_ARGS = {
    "owner": "airflow",
    "depends_on_past": False,
    "email": ["airflow@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
}

dag = DAG(
    dag_id="dag-single-container-env",
    default_args=DEFAULT_ARGS,
    default_view="graph",
    schedule_interval=None,
    start_date=datetime.datetime(2020, 1, 1),
    tags=["example"],
)


#generate dag documentation

dag.doc_md = __doc__

t1 = ECSOperator(
    task_id="Container-orchestration",
    dag=dag,
    aws_conn_id="aws_ecs",
    cluster="hello-world",
    task_definition="XXX",
    launch_type="FARGATE",
    overrides={
	"containerOverrides": [{
		"name": "XXX",
        "command": ["python", "src/bmi_cal_test.py"],
   }]
},
   	network_configuration= {
        "awsvpcConfiguration": {
            "securityGroups": [os.environ.get("SECURITY_GROUP_ID", "XXX")],
            "subnets": [os.environ.get("SUBNET_ID", "XXX")],
            "assignPublicIp" : "ENABLED",
        },
    })