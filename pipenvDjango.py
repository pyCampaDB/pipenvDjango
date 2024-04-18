from subprocess import check_call, CalledProcessError, run as runSubprocess, check_output
from os.path import exists
from os import getenv, getcwd
from pkg_resources import  VersionConflict, DistributionNotFound
from signal import signal, SIGINT
#from getpass import getpass


#########################################################################################################################################3
# evita salir del script al ejecutar Ctrl+C
def signal_handler(sign, frame):
    print('Ctrl+C pressed')

def ensure_pipenv_installed():
    try:
        check_call(['pipenv', '--version'])
        print('pipenv is installed\n')
    except CalledProcessError:
        print('pipenv not found. Install pipenv...')
        check_call(['pip', 'install', 'pipenv'])

def manage_and_use_env():
    if not exists('Pipfile'):
        print('Pipfile not exist. Initializing pipenv environment...\n')
        check_call(['pipenv', 'install'])
    else:

        print('Pipfile exists. Environment ready.\n')


def check_package_installed(package):
    try:
        check_output(['pipenv', 'run', 'pip', 'show', package])
        return True
    except CalledProcessError:
        return False
#Function to install a single package using pipenv
def install_package_with_pipenv(package):
    b = check_package_installed(package)
    if b:
        print(f'\n{package} already installed\n')
    else:
        print(f'\nInstalling {package}...') 
        try:
            runSubprocess(f'pipenv install {package}', shell=True, check=True)
            print(f'\n{package} was installed successfully\n')
        except DistributionNotFound:
            print(f"\nThe package {package} doesn't exist.\nInstalling package...\n")
            runSubprocess(f'pipenv install {package}', shell=True, check=True)
        except VersionConflict as vc:
            installed_version = vc.dist.version
            required_version = vc.req
            print(f"\nA version's conflict detected:\n"
                f"Version installed: {installed_version}"
                f"Version required: {required_version}"
                "Trying to install the package required\n")
            runSubprocess(f'pipenv install --upgrade {package}', shell=True, check=True)
        except CalledProcessError as cp:
            print(f"\nAn error occurred: {cp.returncode}\n")

#Function to install all packages from a requirements.txt file using pipveng
def install_packages_from_file_with_pipenv(file):
    with open (f'{getcwd()}\\{file}.txt', 'r') as myFile:
        for package in myFile.readlines():
            install_package_with_pipenv(package.strip())

        myFile.close()
    

def uninstall_package():
    package = input('Enter the package name: ')
    try:
        runSubprocess(f'pipenv uninstall {package}', shell=True, check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')


def check_packages_installed():
    try:
        runSubprocess('pipenv graph', shell=True, check=True)
    except CalledProcessError as e:
        print(f'An error occurred: {e.returncode}')


def delete_pipenv():
    try:
        runSubprocess('pipenv --rm', shell=True, check=True)
        runSubprocess('del Pipfile', shell=True, check=True)
        runSubprocess('del Pipfile.lock', shell=True, check=True)
    except CalledProcessError as e:
        print(f'An error occurred: {e.returncode}')

def pipenv_run():
    opt = input('pipenv run [your command]. [your command] = ')
    try:
        runSubprocess(f'pipenv run {opt}', shell=True, check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')


def startproject():
    option = input('Enter your project name: ')
    try:
        runSubprocess(f'pipenv run django-admin startproject {option} .',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def startapp():
    option = input('Enter your app name: ')
    try:
        runSubprocess(f'pipenv run python manage.py startapp {option}', 
                      shell=True, 
                      check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def runserver():
    try:
        runSubprocess(f'pipenv run python manage.py runserver',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def migrate():
    try:
        runSubprocess(f'pipenv run python manage.py migrate',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def migrateapp():
    name = input('Enter your app name')
    try:
        runSubprocess(f'pipenv run python manage.py migrate {name}',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def makemigrations(): 
    try:
        runSubprocess(f'pipenv run python manage.py makemigrations',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def makemigrationsapp():
    option = input('Enter your app name: ')
    try:
        runSubprocess(f'pipenv run python manage.py makemigrations {option}',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')
       
def reversemigrateproject():
    option = input('Enter your project name: ')
    try:
        runSubprocess(f'pipenv run python manage.py migrate {option} zero',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def reversemigrateapp():
    option = input('Enter your app name: ')
    try:
        runSubprocess(f'pipenv run python manage.py migrate {option} zero',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def show_migrations():
    try:
        runSubprocess(f'pipenv run python manage.py showmigrations',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def showmigrationsapp():
    option = input('Enter your app name: ')
    try:
        runSubprocess(f'pipenv run python manage.py showmigrations {option}',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def create_superuser():
    try:
        runSubprocess(f'pipenv run python manage.py createsuperuser',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def djangohelp():
    try:
        runSubprocess(f'pipenv run python manage.py help',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def sqlmigrate():
    try:
        appname = input('Enter your app name: ')
        mn = input('Enter the migration number: ')
        runSubprocess(f'pipenv run python manage.py sqlmigrate {appname} {mn}',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def djangoflush():
    try:
        runSubprocess(f'pipenv run python manage.py flush',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def collect_static_files():
    try:
        runSubprocess(f'pipenv run python manage.py collectstatic',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def find_static_file():
    try:
        runSubprocess(f'pipenv run python manage.py findstatic staticfile',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def clearsessions():
    try:
        runSubprocess(f'pipenv run python manage.py clearsessions',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def check_errors():
    try:
        runSubprocess(f'pipenv run python manage.py check',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def changepassword():
    try:
        runSubprocess(f'pipenv run python manage.py changepassword',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def compilemessages():
    try:
        runSubprocess(f'pipenv run python manage.py compilemessages',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def makemessages():
    try:
        runSubprocess(f'pipenv run python manage.py makemessages',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def pythonshell():
    try:
        runSubprocess(f'pipenv run python manage.py shell',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def dbshell():
    try:
        runSubprocess(f'pipenv run python manage.py dbshell',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def inspectdb():
    try:
        runSubprocess(f'pipenv run python manage.py inspectdb',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def load_fixture():
    name = input('Enter your fixture name: ')
    try:
        runSubprocess(f'pipenv run python manage.py loaddata {name}',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def testapp():
    name = input('Enter your app name: ')
    try:
        runSubprocess(f'pipenv run python manage.py test {name}',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def dumpapp():
    name = input('Enter your app name: ')
    try:
        runSubprocess(f'pipenv run python manage.py dumpdata {name}',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def manage_django():
    if not check_package_installed('Django'):
        try:
            runSubprocess('pipenv install Django')
        except CalledProcessError as cp:
            print(f'An error occurred: {cp.returncode}')
         
    option = '1'
    while option in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
                        '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', 
                        '23', '24', '25', '26', '27', '28', '29']:
        option = input(
                '\n************************** DJANGO SETTINGS **************************\n\n'
                '1. Start project\n'
                '2. Start app\n'
                '3. Run server\n'
                '4. Migrate\n'
                '5. Migrate app\n'
                '6. Reverse migration project\n'
                '7. Reverse migration app\n'
                '8. Make migrations\n'
                '9. Make migrations app\n'
                '10. Show migrations\n'
                '11. Show app migrations\n'
                '12. Show the SQL app migration\n'
                '13. Create a superuser\n'
                '14. Collect static files\n'
                '15. Find the absolute path of a static file\n'
                '16. Compile messages\n'
                '17. Make messages\n'
                '18. Check errors\n'
                '19. Run app test\n'
                '20. Delete all data of DB\n'
                '21. Clear the table from expired sessions\n'
                '22. Inspect the DB\n'
                '23. Load data from a fixture\n'
                '24. Create a fixture data app\n'
                '25. Enter in the Python shell\n'
                '26. Enter in the DB shell\n'
                '27. Help\n'
                '28. Change your password\n'
                '(Other) Exit Django Settings\n\n'
                'Enter your choice: ')
            
        if option == '1': startproject()
        elif option == '2': startapp()
        elif option == '3': runserver()
        elif option == '4': migrate()
        elif option == '5': migrateapp()
        elif option == '6': reversemigrateproject()
        elif option == '7': reversemigrateapp()
        elif option == '8': makemigrations()
        elif option == '9': makemigrationsapp()
        elif option == '10': show_migrations()
        elif option == '11': showmigrationsapp()
        elif option == '12': sqlmigrate()
        elif option == '13': create_superuser()
        elif option == '14': collect_static_files()
        elif option == '15': find_static_file()
        elif option == '16': compilemessages()
        elif option == '17': makemessages()
        elif option == '18': check_errors()
        elif option == '19': testapp()
        elif option == '20': djangoflush()
        elif option == '21': clearsessions()
        elif option == '22': inspectdb()
        elif option == '23': load_fixture()
        elif option == '24': dumpapp()
        elif option == '25': pythonshell()
        elif option == '26': dbshell()
        elif option == '27': djangohelp()
        elif option == '28': changepassword()

    print('\n***************************************** EXIT DJANGO SETTINGS *****************************************\n')



def upload_docker():
    username = getenv('DOCKER_USERNAME', default='default_username')
    pwd = getenv('DOCKER_PASSWORD', default='default_password')
    try:
        runSubprocess(['docker', 'login', '--username', username, '--password', pwd], check=True)

        dockerfile_contents = f"""
#Use the official image of Python
FROM python:3.11.0-slim

#Establised your work directory
WORKDIR /app

#Install pipenv
RUN pip install pipenv

#Copy our Pipfile and Pipfile.lock
COPY Pipfile Pipfile.lock /app/

#Installing depends in the system
RUN pipenv install --system --deploy

#Copy all the files
COPY . /app

#Expose the port 8888
EXPOSE 8888

ENV NAME PipEnvironment

CMD pipenv run python pipenvDockerGit.py
    """
        image_name = input('Enter the name of your image: ')

        print('\nWriting Dockerfile\n')
        with open('Dockerfile', 'w') as file:
            file.write(dockerfile_contents)
            file.close()
        print('\nBuilding image...\n')
        runSubprocess(f'docker build -t {image_name}:latest .', shell=True, check=True)
        print('\nImage built.\n')
        runSubprocess(f'docker push {image_name}', shell=True, check=True)
        print('\nImage uploaded to DockerHub.\n')


    except CalledProcessError as cp:
        print(f'CalledProcessError: {cp.returncode}')
    except Exception as e:
        print(f'Exception: {e.__str__}')

def run_container_docker():
    ports = input('ports: ')
    name_container = input('container: ')
    name_img = input('image: ')
    try:
        runSubprocess('pipenv run docker'
                      f' run -p {ports} --name'
                      f' {name_container} {name_img}',
                      shell=True, check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def docker_start():
    container = input('name container: ')
    try:
        runSubprocess('pipenv run docker '
                      f'start {container}', 
                      shell=True, 
                      check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def docker_stop():
    container = input('name container: ')
    try:
        runSubprocess('pipenv run docker stop'
                      f' {container}', 
                      shell=True, check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def docker_restart():
    container = input('name container: ')
    try:
        runSubprocess(f'pipenv run docker restart {container}', 
                      shell=True, check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def docker_ps():
    try:
        runSubprocess('pipenv run docker ps', 
                      shell=True, check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def docker_ps_a():
    try:
        runSubprocess('pipenv run docker ps -a', 
                      shell=True, check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def remove_image():
    img = input(
        '\nEnter the ID of the image: '
    )
    try:
        runSubprocess(f'docker rmi {img}', shell=True, check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def remove_container():
    container = input('\nEnter the ID of the container: ')
    try:
        runSubprocess(f'docker rm {container}', shell=True, check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def exec_it():
    container = input('\nEnter the ID of the container: ')
    try:
        runSubprocess(
            f'docker exec -it {container} bash',
            shell=True,
            check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def show_logs():
    container = input('\nEnter the ID of the container: ')
    try:
        runSubprocess(
            f'docker logs {container}',
            shell=True,
            check=True
        )
    except CalledProcessError as cp:
        print(f'\nAn error occurred: {cp.returncode}')

def docker_pull():
    option = ''
    while option not in ['1', '2', '3']:
        
        option = input(
            '\nOptions:\n'
            '1. Write only the name of the image\n'
            '2. Include a tag\n'
            '3. Include a digest\n'
            '\n'
            'Enter your choice: '
        )
        if option not in ['1', '2', '3']:
            print('\nInvalid option\n')
    

    img = input('Enter the image name: ')
    if option == '2': 
        tag = input('Enter the tag of the image: ')
        try:
            runSubprocess(
                f'docker pull {img}:{tag}',
                shell=True,
                check=True
            )
        except CalledProcessError as cp:
            print(f'An error occurred: {cp.returncode}')

    elif option == '3':
        digest = input('Enter the digest of the image: ')
        try:
            runSubprocess(
                f'docker pull {img}@{digest}',
                shell=True,
                check=True
            )
        except CalledProcessError as cp:
            print(f'An error occurred: {cp.returncode}')

    else:
        try:
            runSubprocess(
                f'docker pull {img}',
                shell=True,
                check=True
            )
        except CalledProcessError as cp:
            print(f'An error occurred: {cp.returncode}')

    
def compose_up():
    try:
        runSubprocess(
            f'docker-compose up',
            shell=True,
            check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def compose_down():
    try:
        runSubprocess(
            'docker-compose down',
            shell=True,
            check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def compose_build():
    try:
        runSubprocess(
            'docker-compose build',
            check=True,
            shell=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def compose_logs():
    try:
        runSubprocess(
            'docker-compose logs',
            shell=True,
            check=True
        )
    except CalledProcessError as cp:
        print (f'An error occurred: {cp.returncode}')

def compose_ps():
    try:
        runSubprocess(
            'docker-compose ps',
            shell=True,
            check=True
        )
    except CalledProcessError as cp:
        print (f'An error occurred: {cp.returncode}')

def compose_restart():
    try:
        services = []
        while True:
            out = input('Enter the amount of containers you want to restart: ')
            if out.isdigit():
                break
        for i in range(int(out)):
            s = input(f'{i} - Enter the name of the container: ')
            services.append(s)
        
        runSubprocess(            
            f'docker-compose restart {services}',
            shell=True,
            check=True
        )
    except CalledProcessError as cp:
        print (f'An error occurred: {cp.returncode}')

def compose_stop():
    try:
        runSubprocess(
            'docker-compose stop',
            shell=True,
            check=True
        )
    except CalledProcessError as cp:
        print (f'An error occurred: {cp.returncode}')

def compose_start():
    try:
        runSubprocess(
            'docker-compose start',
            shell=True,
            check=True
        )
    except CalledProcessError as cp:
        print (f'An error occurred: {cp.returncode}')

def compose_exec():
    service = input('Enter the name of the container: ')
    try:
        runSubprocess(
            f'docker-compose exec {service} bash',
            check=True,
            shell=True
        )

    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def compose_pull():
    try:
        runSubprocess(
        'docker-compose pull',
        shell=True,
        check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def manage_compose():
    print('\n******************************** DOCKER COMPOSE ********************************\n')
    opt = '1'
    while opt in ['1', '2', '3', '4', '5', 
                  '6', '7', '8', '9', '10']:
        opt = input(
            '\n'
            '1. Up docker compose\n'
            '2. Down docker compose\n'
            '3. Build docker compose\n'
            '4. Show the logs of the docker compose\n'
            '5. Show the containers related with docker compose.yml\n'
            '6. Restart docker compose\n'
            '7. Stop docker compose\n'
            '8. Start docker compose\n'
            '9. Exec a command in the running container\n'
            '10. Download the images of the services defined in docker compose.yml\n'
            '(Other) Exit Docker Compose\n\n'
            'Enter your choice: '
        )

        if opt == '1': compose_up()
        elif opt == '2': compose_down()
        elif opt == '3': compose_build()
        elif opt == '4': compose_logs()
        elif opt == '5': compose_ps()
        elif opt == '6': compose_restart()
        elif opt == '7': compose_stop()
        elif opt == '8': compose_start()
        elif opt == '9': compose_exec()
        elif opt == '10': compose_pull()

    print('\n******************************** END DOCKER COMPOSE ********************************\n')

def upload_github():
    try:
        email = getenv("GITHUB_EMAIL", default='default_email')
        runSubprocess(f'git config --global user.email "{email}"',
                      shell=True, check=True)
        print('\nname')
        username = getenv("GITHUB_USERNAME", default='default_username')
        runSubprocess(f'git config --global user.name "{username}"',
                      shell=True, check=True)
        runSubprocess('git init', shell=True, check=True)
        print('\nInitializing Github & git status\n')
        runSubprocess('git status', shell=True, check=True)
        print('\ngit add .\n')
        runSubprocess('git add .', shell=True, check=True)
        commit = input('Enter commit message: ')
        runSubprocess(f'git commit -m "{commit}"', shell=True, check=True)

        first_upload = ''
        while first_upload not in ['Y', 'y', 'N', 'n']:
            first_upload = input('Enter if it is your first commit [Y/N]: ')
            if first_upload not in ['Y', 'y', 'N', 'n']:
                print('\nInvalid option\n')
        
        if first_upload in ['Y', 'y']:
            my_git = input('Enter repository name: ')
            print('\nremote add origin\n')
            #
            runSubprocess(f'git remote add origin https://github.com/pyCampaDB/{my_git}.git',
                shell=True, check=True, capture_output=True)

        print('\npush\n')
        runSubprocess(f'git push -u origin main', shell=True, check=True)
        print('\nProject uploaded to GitHub\n')
    except CalledProcessError as cp:
        print(f'\nCalledProcessError: {cp.returncode}\n')
    except Exception as e:
        print(f'Exeption: {e.__str__}')

def git_remote_v():
    try:
        runSubprocess(
            'git remote -v', shell=True, check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def git_remove_origin():
    try:
        runSubprocess(
            'git remote remove origin',
            shell=True,
            check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def git_clone():
    url = input(
        'Enter the url of the repository: '
    )
    try:
        runSubprocess(
            f'git clone {url}',
            shell= True,
            check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def git_push_origin():
    branch = input(
        'Enter the branch name: '
    )
    try:
        runSubprocess(
            f'git push origin {branch}',
            shell=True,
            check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def git_branch():
    try:
        runSubprocess(
            'git branch',
            shell=True,
            check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def git_checkout():
    try:
        branch = input('Enter the branch name: ')
        runSubprocess(
            f'git checkout {branch}',
            shell=True,
            check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def git_merge():
    try:
        branch = input('Enter the branch name: ')
        runSubprocess(
            f'git merge {branch}',
            shell=True,
            check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')





def cmd():
    command = input(f'{getcwd()}: ')
    try:
        runSubprocess(command, shell=True, check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')
    finally:
        return command

def run():
    signal(SIGINT, signal_handler)

    ensure_pipenv_installed()
    manage_and_use_env()
    option = '1'
    while option in ['1', '2', '3', '4', '5', '6']:
        option = input('\n1. CMD'
                        '\n2. Django Settings'
                       '\n3. Settings pipenv'
                       '\n4. Docker'
                       '\n5. Docker Compose'
                       '\n6. GIT'
                       '\n(Other). Exit\n'
                       '\nEnter your choice: ')
        if option == '1':
            try:
                while True:
                    a = cmd()
                    if a.lower() == 'exit':
                        print('**************************** Exit CMD ************************************')
                        break                 
            except EOFError:
                print('**************************** Exit CMD ************************************')
        elif option == '2':
            manage_django()

        elif option == '3':
            menu = '1'
            while menu in ['1', '2', '3', '4', '5', '6']:
                menu = input('\n*********************************** PIPENV SETTINGS ***********************************\n\n'
                            '\n1. Install an only package'
                            '\n2. Install all packages written in the file'
                            '\n3. Check your packages already installed'
                            '\n4. Uninstall a package'
                            '\n5. Restart your virtual environment'
                            '\n6. Execute your pipenv command'
                            '\n(Other). Exit\n'
                            '\nEnter your choice: ')
                if menu=='1':
                    package = input('\nEnter package name: ')
                    install_package_with_pipenv(package)
                elif menu=='2':
                    file = input('\nEnter the file name: ')
                    install_packages_from_file_with_pipenv(file)
                elif menu=='3':check_packages_installed()
                elif menu=='4':uninstall_package()
                elif menu=='5':
                    delete_pipenv()
                    manage_and_use_env()
                elif menu=='6': pipenv_run()
            print('\n***************************************** EXIT DJANGO SETTINGS *****************************************\n')
        
    
    
        elif option in ['4', '5', '6']:
            from dotenv import load_dotenv
            load_dotenv()
            
            if option == '4':
                docker_option = '1'
                while docker_option in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']:
                    docker_option = input('\n******************** DOCKER: ********************\n'
                                          '1. Upload an image to Docker Hub\n'
                                          '2. Run a docker container\n'
                                          '3. Start docker container\n'
                                          '4. Stop docker container\n'
                                          '5. Restart docker contaienr\n'
                                          '6. Show the containers executing\n'
                                          '7. Show all containers\n'
                                          '8. Remove an image\n'
                                          '9. Remove a container\n'
                                          '10. Show the container\'s logs\n'
                                          '11. Access the virtual environment of your container\n'
                                          '(Other) Exit Docker\n\n'
                                          'Enter your choice: ')
                    if docker_option == '1':upload_docker()
                    elif docker_option == '2': run_container_docker()
                    elif docker_option=='3': docker_start()
                    elif docker_option=='4': docker_stop()
                    elif docker_option=='5': docker_restart()
                    elif docker_option=='6': docker_ps()
                    elif docker_option=='7': docker_ps_a()
                    elif docker_option=='8': remove_image()
                    elif docker_option=='9': remove_container()
                    elif docker_option=='10': show_logs()
                    elif docker_option=='11': exec_it()
                    else: print('\n******************** EXIT DOCKER ********************\n')
                
            elif option == '5': manage_compose()

            elif option == '6':
                git_option = '1'
                while git_option in ['1', '2', '3', '4', '5', '6', '7', '8']:
                    git_option = input(
                        '\n******************** GIT ********************\n\n'
                        '1. Upload your project to GitHub\n'
                        '2. git remote -v\n'
                        '3. git remote remove origin\n'
                        '4. git clone\n'
                        '5. Send local commits to a remote repository\n'
                        '6. git checkout\n'
                        '7. git merge\n'
                        '8. Display the availables local branches of the repository'
                        '\n'
                        '(Other) Exit GIT\n\n'
                        'Enter your choice: '
                    )

                    if git_option == '1':
                        upload_github()
                    elif git_option == '2': git_remote_v()
                    elif git_option == '3': git_remove_origin()
                    elif git_option == '4': git_clone()
                    elif git_option == '5': git_push_origin()
                    elif git_option == '6': git_checkout()
                    elif git_option == '7': git_merge()
                    elif git_option == '8': git_branch()
                print('\n******************** EXIT GIT ********************\n\n')


############################################# MAIN ##########################################################################
if __name__ == '__main__':
    run()


