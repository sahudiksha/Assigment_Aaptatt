import json
import requests

def get_pull_requests_between_releases(owner, repo, release_version_start, release_version_end, github_token):
    url = f'https://api.github.com/repos/{owner}/{repo}/pulls'
    headers = {'Authorization': f'token {github_token}'}
    pull_requests = []

    page = 1
    per_page = 100 

    while True:
        response = requests.get(url, headers=headers, params={'page': page, 'per_page': per_page, 'state': 'all'})

        if response.status_code == 200:     
            page_pull_requests = response.json()
            if not page_pull_requests:
                break  

            for pr in page_pull_requests:
                pr_labels = [label['name'] for label in pr.get('labels', [])]
                if any(label in pr_labels for label in [release_version_start, release_version_end]):
                    pr_details_response = requests.get(pr['url'], headers=headers)
                    if pr_details_response.status_code == 200:
                        pull_requests.append(pr_details_response.json())
            page += 1
        else:
            print(f'Failed to fetch pull requests. Status code: {response.status_code}')
            return None

    return pull_requests

if __name__ == "__main__":
    with open('config.json') as config_file:
        config = json.load(config_file)

    owner, repo, release_version_start, release_version_end, github_token = \
        config.get('owner'), config.get('repo'), config.get('release_version_start'), config.get('release_version_end'), config.get('github_token')

    pull_requests = get_pull_requests_between_releases(owner, repo, release_version_start, release_version_end, github_token)
    if pull_requests:
        total_pull_requests_msg = f'Total pull requests between {release_version_start} and {release_version_end}: {len(pull_requests)}'
        print(total_pull_requests_msg)
        output_file = 'pull_requests.txt'
        with open(output_file, 'w') as f:
            f.write(f'Total pull requests between {release_version_start} and {release_version_end}: {len(pull_requests)}\n')
            f.write("Pull Requests:\n")
            for pr in pull_requests:
                f.write(f'- #{pr["number"]}: {pr["title"]} by {pr["user"]["login"]}\n')
                f.write(f'  URL: {pr["html_url"]}\n')
                f.write(f'  State: {pr["state"]}\n')
                f.write(f'  Description: {pr["body"]}\n\n' if pr.get("body") else '\n')
        print(f'Pull requests details are saved in {output_file}')
    else:
        print('Failed to retrieve pull requests.')
