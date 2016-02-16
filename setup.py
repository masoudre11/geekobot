from setuptools import setup

setup(name='Geekobot',
      version='1.0',
      description='OpenShift App',
      author='Pooya Eghbali',
      author_email='example@example.com',
      url='http://www.python.org/sigs/distutils-sig/',
      install_requires=['pyTelegramBotAPI>=1.4.1',
                        'wikipedia>=1.4.0',
                        'textblob>=0.11.0',
                        'pyowm>=2.3.0',
                        'py-expression-eval>=0.3.0',
                        'pyquery>=1.2.10',
                        'atg>=0.0.6',
                        'flask>=0.10.1'],
     )
