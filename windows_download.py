# coding: utf-8
import urllib.request
import requests
import subprocess


def spigot(version, java):
    burl = 'https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar'
    save_name = "buildtools.jar"
    urllib.request.urlretrieve(burl, save_name)
    subprocess.run((f'{java}', '-jar', 'buildtools.jar', '--rev', f'{version}'), check=False)
