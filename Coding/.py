import json
import os
import argparse
from datetime import datetime

TASKS_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)

def add_task(description):
    tasks = load_tasks()
    new_id = max([task['id'] for task in tasks], default=0) + 1
    now = datetime.now().isoformat()
    tasks.append({
        'id': new_id,
        'description': description,
        'status': 'todo',
        'createdAt': now,
        'updatedAt': now
    })
    save_tasks(tasks)
    print(f"Προστέθηκε εργασία #{new_id}: {description}")

def list_tasks(status_filter=None):
    tasks = load_tasks()
    if not tasks:
        print("Δεν υπάρχουν εργασίες.")
        return

    filtered_tasks = tasks
    if status_filter:
        filtered_tasks = [task for task in tasks if task['status'] == status_filter]

    if not filtered_tasks:
        print(f"Δεν υπάρχουν εργασίες με κατάσταση '{status_filter}'.")
        return

    for task in filtered_tasks:
        print(f"[{task['id']}] ({task['status']}) {task['description']}")
        print(f"  Δημιουργήθηκε: {task['createdAt']}")
        print(f"  Ενημερώθηκε: {task['updatedAt']}")

def update_status(task_id, new_status):
    tasks = load_tasks()
    now = datetime.now().isoformat()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = new_status
            task['updatedAt'] = now
            save_tasks(tasks)
            print(f"Η εργασία #{task_id} ενημερώθηκε σε '{new_status}'.")
            return
    print(f"Δεν βρέθηκε εργασία με id #{task_id}")

def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    print(f"Η εργασία #{task_id} διαγράφηκε.")

def main():
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    subparsers = parser.add_subparsers(dest='command')

    parser_add = subparsers.add_parser('add')
    parser_add.add_argument('title')

    parser_list = subparsers.add_parser('list')
    parser_list.add_argument('--status', choices=['todo', 'doing', 'done'], help="Filter tasks by status")

    parser_update = subparsers.add_parser('update')
    parser_update.add_argument('id', type=int)
    parser_update.add_argument('status', choices=['todo', 'doing', 'done'])

    parser_delete = subparsers.add_parser('delete')
    parser_delete.add_argument('id', type=int)

    args = parser.parse_args()

    if args.command == 'add':
        add_task(args.title)
    elif args.command == 'list':
        list_tasks(args.status)
    elif args.command == 'update':
        update_status(args.id, args.status)
    elif args.command == 'delete':
        delete_task(args.id)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
