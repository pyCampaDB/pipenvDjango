from subprocess import check_call, CalledProcessError, run as runSubprocess, check_output
from os.path import exists
from os import getenv, getcwd
from pkg_resources import  VersionConflict, DistributionNotFound


#########################################################################################################################################3
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
    


def check_packages_installed():
    try:
        runSubprocess('pipenv graph', shell=True, check=True)
    except CalledProcessError as e:
        print(f'An error ocurred: {e.stderr.decode()}')


def delete_pipenv():
    try:
        runSubprocess('pipenv --rm', shell=True, check=True)
        runSubprocess('del Pipfile', shell=True, check=True)
        runSubprocess('del Pipfile.lock', shell=True, check=True)
    except CalledProcessError as e:
        print(f'An error ocurred: {e.stderr.decode()}')

def startproject():
    option = input('Enter your project name: ')
    try:
        runSubprocess(f'pipenv run django-admin startproject {option} .',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error ocurred: {cp}')

def startapp():
    option = input('Enter your app name: ')
    try:
        runSubprocess(f'pipenv run python manage.py startapp {option}', 
                      shell=True, 
                      check=True)
    except CalledProcessError as cp:
        print(f'An error ocurred: {cp}')

def runserver():
    try:
        runSubprocess(f'pipenv run python manage.py runserver',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error ocurred: {cp}')

def migrate():
    try:
        runSubprocess(f'pipenv run python manage.py migrate',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error ocurred: {cp}')

def makemigrations(): 
    try:
        runSubprocess(f'pipenv run python manage.py makemigrations',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error ocurred: {cp}')

def makemigrationsapp():
    option = input('Enter your app name: ')
    try:
        runSubprocess(f'pipenv run python manage.py makemigrations {option}',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error ocurred: {cp}')


def migrate_app():
    option = input('Enter your app name: ')
    try:
        runSubprocess(f'pipenv run python manage.py migrate {option}',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error ocurred: {cp}')

def show_migrations():
    try:
        runSubprocess(f'pipenv run python manage.py showmigrations',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error ocurred: {cp}')

def showmigrationsapp():
    option = input('Enter your app name: ')
    try:
        runSubprocess(f'pipenv run python manage.py showmigrations {option}',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error ocurred: {cp}')


def create_superuser():
    try:
        runSubprocess(f'pipenv run python manage.py createsuperuser',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error ocurred: {cp}')

def shell_django():
    try:
        runSubprocess(f'pipenv run python manage.py shell',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error ocurred: {cp}')


def manage_django():
    option = '1'
    while option in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']:
        option = input(
            '\n************************** DJANGO SETTINGS **************************\n\n'
              '1. Start project\n'
              '2. Start app\n'
              '3. Run server\n'
              '4. Migrate\n'
              '5. Migrate app\n'
              '6. Migrate app zero\n'
              '7. Make migrations\n'
              '8. Show migrations\n'
              '9. Show app migrations\n'
              '10. Create a superuser\n'
              '11. Enter in the shell manage.py\n'
              '(Other) Exit Django Settings\n\n'
              'Enter your choice: ')
        
        if option == '1':
            startproject()
        elif option == '2':
            startapp()
        elif option == '3':
            runserver()
        elif option == '4':
            migrate()
        elif option == '5':
            migrate_app()
        elif option == '6':
            makemigrationsapp()
        elif option == '7':
            makemigrations()
        elif option == '8':
            show_migrations()
        elif option == '9':
            showmigrationsapp()
        elif option == '10':
            create_superuser()
        elif option == '11':
            shell_django()
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
        print(f'CalledProcessError: {cp.stderr}')
    except Exception as e:
        print(f'Exception: {e}')

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

        print('\ngit branch\n')
        runSubprocess('git branch -M main', shell=True, check=True)
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
        else:
            print('\npull\n')
            runSubprocess('git pull origin main', shell=True, check=True)
        print('\npush\n')
        runSubprocess(f'git push -u origin main', shell=True, check=True)
        print('\nProject uploaded to GitHub\n')
    except CalledProcessError as cp:
        print(f'\nCalledProcessError: {cp.stderr}\n')
    except Exception as e:
        print(f'Exeption: {e}')


def run():
    ensure_pipenv_installed()
    manage_and_use_env()
    option = '1'
    while option in ['1', '2']:
        option = input('\n1. Django Settings'
                       '\n2. Settings pipenv'
                       '\n(Other). Exit'
                       '\nEnter your choice: ')
        """if option not in ['1', '2']:
            print('\ninvalid option\n')"""
        if option == '2':
            menu = '1'
            while menu in ['1', '2', '3', '4']:
                menu = input('\n*********************************** PIPENV SETTINGS ***********************************\n\n'
                            '\n1. Install an only package'
                            '\n2. Install all packages written in the file'
                            '\n3. Check your packages already installed'
                            '\n4. Restart your virtual environment'
                            '\n(Other). Exit setting pipenv and run script\n'
                            '\nEnter your choice: ')
                if menu=='1':
                    package = input('\nEnter package name: ')
                    install_package_with_pipenv(package)
                elif menu=='2':
                    file = input('\nEnter the file name: ')
                    install_packages_from_file_with_pipenv(file)
                elif menu=='3':
                    check_packages_installed()
                elif menu=='4':
                    delete_pipenv()
                    manage_and_use_env()
            print('\n***************************************** EXIT DJANGO SETTINGS *****************************************\n')
        elif option == '1':
            manage_django()
    
    from dotenv import load_dotenv
    load_dotenv()
    docker_option = '9'
    while docker_option not in ['Y', 'y', 'N', 'n']:
        docker_option = input('Do you want to upload this project to Docker? [Y/N]: ')
        if docker_option not in ['Y', 'y', 'N', 'n']:
            print('\nInvalid option\n')
    if docker_option in ['Y', 'y']:
        upload_docker()
    else:
        print('\nDocker pass...\n')

    git_option = '9'
    while git_option not in ['Y', 'y', 'N', 'n']:
        git_option = input('Do you want to upload this project to GitHub? [Y/N]: ')
        if git_option not in ['Y', 'y', 'N', 'n']:
            print('\nInvalid option\n')
    if git_option in ['Y', 'y']:
        upload_github()
    else:
        print('\nGit pass...\n')

############################################# MAIN ##########################################################################
if __name__ == '__main__':
    run()

