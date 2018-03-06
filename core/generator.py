import subprocess
from jinja2 import FileSystemLoader, Environment

class Generator(object):
    def create(self,package,scriptfile):
        self.package = package
        self.scriptfile = scriptfile
        self.DEBIAN = 'packages/{}/DEBIAN'.format(self.package)
        self.SCRIPT = 'packages/{}/var/cache/apt/archives'.format(self.package)
        subprocess.check_output('mkdir -p {}'.format(self.DEBIAN).split())
        subprocess.check_output('mkdir -p {}'.format(self.SCRIPT).split())
        subprocess.check_output('cp {} {}/{}.sh'.format(self.scriptfile,self.SCRIPT,self.package).split())
        self.control()
        self.postinst()
        subprocess.check_output('dpkg-deb --build packages/{} debs/'.format(self.package).split())

    def control(self,):
        open('{}/control'.format(self.DEBIAN),'w').write(Template('control').render({'PACKAGE':self.package}))

    def postinst(self):
        open('{}/postinst'.format(self.DEBIAN),'w').write(Template('postinst').render({'PACKAGE':self.package}))
        subprocess.check_output('chmod 755 {}/postinst'.format(self.DEBIAN).split())

class Template(object):
    def __new__(self,name):
        template_engine = Environment(loader=FileSystemLoader("templates"))
        return template_engine.get_template(name)
