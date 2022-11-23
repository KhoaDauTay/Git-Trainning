from diagrams import Diagram, Cluster, Edge
from diagrams.digitalocean.storage import Folder
from diagrams.onprem.vcs import Github, Git

with Diagram("App Dev"):
    repo = Github("Repository")

    with Cluster("Working dir"):
        my_folder = Folder("Code")

    with Cluster("Staging dir"):
        staging_dir = Folder("My code")

    with Cluster("Local repository"):
        local_repo = Git("Local")

    my_folder >> staging_dir >> local_repo

