#!/usr/bin/env python

# email : elwafi.courrier99@gmail.com
# maintainer : El Wafi El Mehdi
# date : 09/02/2023
# description : script for CLI app for managing notes

import os
import sys
import csv
import datetime

csv_headers = ['id','datetime','title','body']

arguments=sys.argv[1:]

working_dir = os.path.join(os.getenv("HOME"),".pnote/")

db_file= os.path.join(working_dir,"notes.csv")

def usage():
    print("""
Usage:  pnote [options] <subcommand> [args]

Main commands:
    new     create a new note
    rm ID   remove a note by id
    ls      list user's notes
    desc ID describe a note by id
""")
    exit(1)


def load_csv_database(working_dir,csv_path):

    if not os.path.isdir(working_dir):

        os.makedirs(working_dir)

        with open(csv_path,'w') as f_db:
            csv_writer = csv.writer(f_db)
            csv_writer.writerow(csv_headers)
        
    elif not os.path.isfile(db_file):

        with open(csv_path,'w') as f_db:
            csv_writer = csv.writer(f_db)
            csv_writer.writerow(csv_headers)


def list_notes(csv_path):

    with open(csv_path,'r') as db_f:
        csv_reader = csv.DictReader(db_f)
        for note in csv_reader:
            print(f"{  note['id'] } \t {note['datetime'] } \t { note['title'] } \t { note['body'] }\n")
            
def generate_note_id(csv_path):
    ids = [0]
    with open(csv_path) as f:
        csv_reader = csv.DictReader(f)
        for note in csv_reader:
            ids.append(int(note['id']))
    return max(ids) + 1

def create_note(csv_path,note_title,note_body):
    note = { "id": generate_note_id(csv_path) ,"datetime": str(datetime.datetime.now()), "title": note_title, "body": note_body}
    
    with open(csv_path,'a') as db_f:
        csv_writer = csv.DictWriter(db_f,fieldnames=csv_headers)
        csv_writer.writerow(note)

def describe_note(note_id,db_f):
    with open(db_f) as f:
        csv_reader = csv.DictReader(f)
        for note in csv_reader:
            if int(note["id"]) == note_id:
                print(f"{ note['id'] }\t {note['datetime'] } \t { note['title'] } \n\n{ note['body'] }\n")

def delete_note(note_id,db_f):
    describe_note(note_id,db_f)
    prompt = input("Are you sure you want to delete this note? [Yes-No]:")
    if prompt == 'Yes':
        with open(db_f,'r') as f:
            lines = f.readlines()
            
        for line in lines:
            if line.startswith('id'):
                continue
            values = line.split(',')
            print(values)
            if int(values[0]) == note_id:
                lines.remove(line)
                break

        with open(db_f,'w') as f:
            f.writelines(lines)
    else:
        pass


load_csv_database(working_dir,db_file)

if len(arguments) < 1:
    usage()

match arguments[0]:
    case "ls":
        list_notes(db_file)
        exit(0)
    case "desc":
        describe_note(int(arguments[1]),db_file)
        exit(0)
    case "new":
        create_note(db_file,arguments[1],arguments[2])
    case "rm":
        delete_note(int(arguments[1]),db_file)
        exit(0)
    case _:
        usage()


