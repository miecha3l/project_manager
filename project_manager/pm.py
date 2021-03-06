import sys
import os
import common.services.config as config
import common.services.arg_processor as arg_processor
import common.directory_manager as directory_manager

def run():
    cfg = config.load()
    args = arg_processor.parse()
    paths = directory_manager.create_dirs(cfg, args)
    if paths is None:
        print("Project with that name already exists")
        exit(0)

    print("New {tech} project created: {path}".format(tech=args.tech, path=paths['proj']))

    if not args.no_repo:
        init_repo(paths['repo'], args.project_name)
        print("Git repository initialized with readme.md")

    directory_manager.create_custom_schemas(cfg, args, paths['repo'], paths['proj'])
    additional_actions(args, paths['repo'])
        

def init_repo(repo_path, project_name):
    with open(repo_path + '\\readme.md', 'w') as readme:
        readme.write('# {project_name}\n'.format(project_name=project_name))
    os.system('cd {path} && git init && git add . && git commit -m \"initial commit\"'.format(path=repo_path))

def additional_actions(args, repo_path):
    if args.open_vsc:
        os.system('cd {path} && code .'.format(path=repo_path))
    
    if args.open_dir:
        os.system('start {path}'.format(path=repo_path))

if __name__ == '__main__':
    run()

    

            
    
    
