"""
API MAPPING FOR Watson APIs
"""

mapping_table = {

    'content_type': 'application/json',
    'path_prefix': '',

    'tone_analyzer_tone': {
        'content_type': 'text/plain',
        'path': '/tone-analyzer/api/v3/tone',
        'valid_params': ['version','tones','sentences']
    },

}
