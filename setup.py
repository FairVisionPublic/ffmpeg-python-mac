from setuptools import setup, find_packages
from textwrap import dedent

version = '0.0.1'
download_url = 'https://github.com/FAIR-VISION/ffmpeg-python/archive/refs/heads/main.zip'.format(
    version
)

long_description = dedent(
    '''\
    ffmpeg-python: Python bindings for FFmpeg
    =========================================

    '''
)


file_formats = [
    'aac',
    'ac3',
    'avi',
    'bmp',
    'flac',
    'gif',
    'mov',
    'mp3',
    'mp4',
    'png',
    'raw',
    'rawvideo',
    'wav',
]
file_formats += ['.{}'.format(x) for x in file_formats]

misc_keywords = [
    '-vf',
    'a/v',
    'audio',
    'dsp',
    'FFmpeg',
    'ffmpeg',
    'ffprobe',
    'filtering',
    'filter_complex',
    'movie',
    'render',
    'signals',
    'sound',
    'streaming',
    'streams',
    'vf',
    'video',
    'wrapper',
]

keywords = misc_keywords + file_formats

setup(
    name='ffmpeg-python',
    packages=['ffmpeg', 'ffmpeg.third_part'],
    include_package_data=True,
    package_data={'ffmpeg.third_part': ['*.exe']},
    setup_requires=['pytest-runner'],
    version=version,
    description='Python bindings for FFmpeg fv soft',
    author='extstagiaire1',
    author_email='support@fairvision.fr',
    url='https://github.com/FAIR-VISION/ffmpeg-python.git',
    download_url=download_url,
    keywords=keywords,
    long_description=long_description,
    install_requires=['future'],
    extras_require={
        'dev': [
            'future==0.17.1',
            'numpy==1.16.4',
            'pytest-mock==1.10.4',
            'Sphinx==2.1.0',
            'tox==3.12.1',
        ]
    },
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
