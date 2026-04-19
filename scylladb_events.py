# ScyllaDB-ə sosial hadisə yazmaq (Python)

from cassandra.cluster import Cluster
from datetime import datetime

cluster = Cluster(['scylladb-cloud-host'])
session = cluster.connect('supercell_id')

def store_social_event(player_id, event_type, data):
    session.execute(
        '''
        INSERT INTO social_events
            (player_id, event_type, payload, created_at)
        VALUES (%s, %s, %s, %s)
        ''',
        (player_id, event_type, data, datetime.utcnow())
    )

# Dost istəyini saxlamaq
store_social_event(
    player_id='P12345',
    event_type='FRIEND_REQUEST',
    data='{"from": "P67890"}'
)
