from subprocess import check_call, CalledProcessError, run as runSubprocess, check_output
from os.path import exists
from os import getenv, getcwd
from pkg_resources import  VersionConflict, DistributionNotFound
from dotenv import load_dotenv


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
#
def migrateapp():
    name = input('Enter your app name')
    try:
        runSubprocess(f'pipenv run python manage.py migrate {name}',
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
       
def reversemigrateproject():
    option = input('Enter your project name: ')
    try:
        runSubprocess(f'pipenv run python manage.py migrate {option} zero',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error ocurred: {cp}')

def reversemigrateapp():
    option = input('Enter your app name: ')
    try:
        runSubprocess(f'pipenv run python manage.py migrate {option} zero',
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

def djangohelp():
    try:
        runSubprocess(f'pipenv run python manage.py help',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error ocurred: {cp}')

def sqlmigrate():
    try:
        appname = input('Enter your app name: ')
        mn = input('Enter the migration number: ')
        runSubprocess(f'pipenv run python manage.py sqlmigrate {appname} {mn}',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error ocurred: {cp}')

def djangoflush():
    try:
        runSubprocess(f'pipenv run python manage.py flush',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error ocurred: {cp}')

def collect_static_files():
    try:
        runSubprocess(f'pipenv run python manage.py collectstatic',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error ocurred: {cp}')

def find_static_file():
    try:
        runSubprocess(f'pipenv run python manage.py findstatic staticfile',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error ocurred: {cp}')

def clearsessions():
    try:
        runSubprocess(f'pipenv run python manage.py clearsessions',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error ocurred: {cp}')

def check_errors():
    try:
        runSubprocess(f'pipenv run python manage.py check',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error ocurred: {cp}')

def changepassword():
    try:
        runSubprocess(f'pipenv run python manage.py changepassword',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error ocurred: {cp}')

def compilemessages():
    try:
        runSubprocess(f'pipenv run python manage.py compilemessages',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error ocurred: {cp}')

def makemessages():
    try:
        runSubprocess(f'pipenv run python manage.py makemessages',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error ocurred: {cp}')

def pythonshell():
    try:
        runSubprocess(f'pipenv run python manage.py shell',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error ocurred: {cp}')

def dbshell():
    try:
        runSubprocess(f'pipenv run python manage.py dbshell',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error ocurred: {cp}')

def inspectdb():
    try:
        runSubprocess(f'pipenv run python manage.py inspectdb',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error ocurred: {cp}')

def load_fixture():
    name = input('Enter your fixture name: ')
    try:
        runSubprocess(f'pipenv run python manage.py loaddata {name}',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error ocurred: {cp}')

def testapp():
    name = input('Enter your app name: ')
    try:
        runSubprocess(f'pipenv run python manage.py test {name}',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error ocurred: {cp}')

def dumpapp():
    name = input('Enter your app name: ')
    try:
        runSubprocess(f'pipenv run python manage.py dumpdata {name}',
                      shell=True,
                      check=True)
    except CalledProcessError as cp:
        print(f'An error ocurred: {cp}')

def manage_django():
    option = '1'
    while option in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
                     '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', 
                     '23', '24', '25', '26', '27', '28']:
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

        first_upload = ''
        while first_upload not in ['Y', 'y', 'N', 'n']:
            first_upload = input('Enter if it is your first commit [Y/N]: ')
            if first_upload not in ['Y', 'y', 'N', 'n']:
                print('\nInvalid option\n')
        
        if first_upload in ['Y', 'y']:
            print('\ngit branch\n')
            runSubprocess('git branch -M main', shell=True, check=True)
            my_git = input('Enter repository name: ')
            print('\nremote add origin\n')
            runSubprocess(f'git remote add origin https://github.com/pyCampaDB/{my_git}.git',
                shell=True, check=True, capture_output=True)

        print('\npush\n')
        runSubprocess(f'git push -u origin main', shell=True, check=True)
        print('\nProject uploaded to GitHub\n')
    except CalledProcessError as cp:
        print(f'\nCalledProcessError: {cp.stderr}\n')
    except Exception as e:
        print(f'Exeption: {e}')


def run():
    load_dotenv()
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
                            '\n(Other). Exit pipenv settings\n'
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


