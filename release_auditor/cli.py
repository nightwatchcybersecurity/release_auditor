#
# Copyright (c) 2021 Nightwatch Cybersecurity.
#
# This file is part of release_auditor
# (see https://github.com/nightwatchcybersecurity/release_auditor).
#
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
#
import sys

from dateutil import parser
import click
from github import Github
from release_auditor.utils import ReleaseAuditorUtils


@click.version_option(version=ReleaseAuditorUtils.get_version(), prog_name='release_auditor')
@click.group()
def cli():
    """
    release_auditor - A tool for checking if GitHub release assets were modified after publication.

    Copyright (c) 2021 Nightwatch Cybersecurity.
    Source code: https://github.com/nightwatchcybersecurity/release_auditor
    """
    # TODO: Add input validation
    # TODO: Add unit tests


@cli.command('github')
@click.option('--verbose', is_flag=True, help='Output more details')
@click.argument('repository', required=True)
@click.option('--base_url', help='URL of the GitHub instance')
@click.option('--login_or_token', help='GitHub username or access token')
@click.option('--password', help='GitHub password')
@click.option('--hours', default=24, help='Number of hours to check for', type=click.INT)
@click.option('--max', default=5, help='Maximum number of releases to check', type=click.INT)
def github(verbose, repository, base_url, login_or_token, password, hours, max):
    """Audits GitHub releases"""
    # Get release info
    print("Retrieving repository and release information")
    if base_url:
        gh = Github(base_url=base_url, login_or_token=login_or_token, password=password)
    else:
        gh = Github(login_or_token=login_or_token, password=password)
    repo = gh.get_repo(repository)
    releases = repo.get_releases().get_page(0)

    # Iterate through releases
    issues_found = False
    if max < len(releases):
        releases = releases[:max]
    print("Checking the first " + str(len(releases)) + " releases")
    for release in releases:
        click.echo("\nChecking release: " + release.title)
        if verbose:
            click.echo("Created by '" + release.author.login + "' at " + str(release.created_at)
                  + ", published at " + str(release.published_at))

        # Checking assets
        if len(release.raw_data['assets']) == 0:
            click.echo('-- No assets found, skipping release')
            continue

        for asset in release.raw_data['assets']:
            if verbose:
                click.echo("- Checking asset: " + asset['name'] + ", created by '" + asset['uploader']['login'] +
                           "' at " + asset['created_at'] + ", published at " + asset['updated_at'])

            # Check author name
            if asset['uploader']['login'] != release.author.login:
                click.echo("--- Release author '" + release.author.login + "' not the same as asset uploader '"
                           + asset['uploader']['login'] + "'")
                issues_found = True

            # Check date differences
            created_diff = parser.isoparse(asset['created_at']).replace(tzinfo=None) - release.published_at
            updated_diff = parser.isoparse(asset['updated_at']).replace(tzinfo=None) - release.published_at
            if created_diff.seconds > hours*3600 or updated_diff.seconds > hours*3600:
                click.echo("--- Asset was created or updated more than " + hours +
                           " hours after the release was published")
                issues_found = True

    # Return error if issues found
    if issues_found:
        sys.exit(-1)


if __name__ == '__main__':
    cli(prog_name='release_auditor')
