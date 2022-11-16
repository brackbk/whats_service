
# utils
import os
import sys
import json
# GCP
from google.cloud import pubsub_v1

class Queue:
    def __init__(
            self,
            TOPIC,
            PROJECT_ID
        ):
        self.topic = TOPIC
        self.project_id = PROJECT_ID
    
    def publish(self, payload):
        topic_name = 'projects/{project_id}/topics/{topic}'.format(
            project_id=self.project_id,
            topic=self.topic, 
        )

        # Encodes message
        encoded = json.dumps(payload).encode("utf-8")

        # Publisher
        publisher = pubsub_v1.PublisherClient()
        publisher.publish(topic_name, data=encoded)
