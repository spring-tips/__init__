#!/usr/bin/env python 

import os, sys, time, re 

if __name__ == '__main__' :
    root = 'spring-tips'
    repositories = 'https://github.com/%s/__init__/blob/master/repositories.txt' % root 

    def generate_init_repository() :
        readme_txt = '''
    mkdir %s && cd %s && curl https://raw.githubusercontent.com/%s/__init__/master/start.sh | bash
        ''' % ( root,root,root)
        readme_txt = readme_txt.strip().lstrip()
        with open( 'README.md', 'w') as fp :
            fp.writelines([os.linesep])
            fp.writelines(['# Start Here' ])
            fp.writelines([os.linesep])
            fp.write(  '```%s```' % readme_txt)
            fp.writelines([os.linesep])
    
    def generate_start():
        start = '''
#!/usr/bin/env bash 

REPOSITORIES_TEXT=%s
GIT_TEMPLATE_ROOT=git@github.com:%s
start=$( cd `dirname $0` && pwd	 )
echo "initializing from ${start} "
curl https://raw.githubusercontent.com/%s/__init__/master/repositories.txt | while read l ; do
    d=$(echo $l | cut -f5 -d\/ | cut -f1 -d\. ) 
    echo "Processing $d"  
    dir_to_create=${start}/$d
    if [[ -e  $dir_to_create ]] ; then 
        echo "WARN: ${dir_to_create} aleady exists." 
    else
        echo "initializing ${dir_to_create}"  
        git_repo=${GIT_TEMPLATE_ROOT}/${d}.git
        git clone ${git_repo} ${dir_to_create}
    fi
done 
        '''  .strip() % (repositories, root, root )
        with open( 'start.sh', 'w') as fp : 
            fp.write ( start)
            fp.writelines([os.linesep])




    generate_init_repository()
    generate_start()
