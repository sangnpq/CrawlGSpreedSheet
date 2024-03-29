import datetime

class User():
    data = {
        'id': 0,
        'id_chat': '',
        'username': '',
        'display_name': '',
        'avatar': '',
        'cover': '',
        'gender': '',
        'birthday': '',
        'location': '',
        'post_count': '',
        'friend_count': '',
        'status': '',
        'create_time': '',
        'relation': '',
        'status_verify': '',
        'data_source': '',
        'work': '',
        'relationship': '',
        'province': '',
        'website': '',
        'education': '',
        'update_time': str(datetime.datetime.now())
        
    }
    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key == 'counts':
                if kwargs['counts']:
                    for key1 in kwargs['counts'].keys():
                        self.data[key1] = kwargs['counts'][key1]
            elif key == 'user_info':
                if kwargs['user_info']:
                    for key2 in kwargs['user_info'].keys():
                        self.data[key2] = kwargs['user_info'][key2]
            else:
                self.data[key] = kwargs[key]
    def get_value(self):
        attr = [ 'id', 'id_chat','username', 'display_name', 'avatar', 
        'cover', 'gender', 'birthday', 'location', 'post_count', 
        'friend_count', 'status', 'create_time', 'relation',
        'status_verify', 'data_source', 'work', 'relationship', 
        'province', 'website', 'education', 'update_time']

        return [ self.data[key] for key in attr ]
