# coding: utf-8
from __future__ import unicode_literals

from datetime import datetime
import base64

from .common import InfoExtractor
from ..utils import (
    HEADRequest,
    urlencode_postdata,
)


class TenPlayIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?10play\.com\.au/(?:[^/]+/)+(?P<id>tpv\d{6}[a-z]{5})'
    _NETRC_MACHINE = '10play'
    _TESTS = [{
        'url': 'https://10play.com.au/todd-sampsons-body-hack/episodes/season-4/episode-7/tpv200921kvngh',
        'info_dict': {
            'id': '6192880312001',
            'ext': 'mp4',
            'title': "Todd Sampson's Body Hack - S4 Ep. 2",
            'description': 'md5:fa278820ad90f08ea187f9458316ac74',
            'age_limit': 15,
            'timestamp': 1600770600,
            'upload_date': '20200922',
            'uploader': 'Channel 10',
            'uploader_id': '2199827728001'
        },
        'params': {
            'skip_download': True,
        }
    }, {
        'url': 'https://10play.com.au/how-to-stay-married/web-extras/season-1/terrys-talks-ep-1-embracing-change/tpv190915ylupc',
        'only_matching': True,
    }]
    _GEO_BYPASS = False

    _AUS_AGES = {
        'G': 0,
        'PG': 15,
        'M': 15,
        'MA': 15,
        'R': 18,
        'X': 18
    }

    def _get_bearer_token(self, video_id):
        username, password = self._get_login_info()
        if username is None or password is None:
            self.raise_login_required('Your 10play account\'s details must be provided with --username and --password.')
        _timestamp = datetime.now().strftime('%Y%m%d000000')
        _auth_header = base64.b64encode(_timestamp.encode('ascii')).decode('ascii')
        data = self._download_json('https://10play.com.au/api/user/auth', video_id, 'Getting bearer token', headers={
            'X-Network-Ten-Auth': _auth_header,
        }, data=urlencode_postdata({
            'email': username,
            'password': password,
        }))
        return "Bearer " + data['jwt']['accessToken']

    def _real_extract(self, url):
        content_id = self._match_id(url)
        _token = self._get_bearer_token(content_id)
        data = self._download_json(
            'https://10play.com.au/api/v1/videos/' + content_id, content_id)
        _video_url = self._download_json(
            data.get('playbackApiEndpoint'), content_id, 'Downloading video JSON',
            headers={'Authorization': _token}).get('source')
        m3u8_url = self._request_webpage(HEADRequest(
            _video_url), content_id).geturl()
        if '10play-not-in-oz' in m3u8_url:
            self.raise_geo_restricted(countries=['AU'])
        formats = self._extract_m3u8_formats(m3u8_url, content_id, 'mp4')
        self._sort_formats(formats)

        return {
            'formats': formats,
            'id': data.get('altId') or content_id,
            'title': data.get('title'),
            'description': data.get('description'),
            'age_limit': self._AUS_AGES[data.get('classification')],
            'series': data.get('showName'),
            'season': data.get('showContentSeason'),
            'timestamp': data.get('published'),
            'thumbnail': data.get('imageUrl'),
            'uploader': 'Channel 10',
            'uploader_id': '2199827728001',
        }
