"""
Create 2 separate charts for student data and course data:
  student:
    add id
    name
    gpa
    birth 
  course:
    id
    name
"""
import psycopg2 as pg

CONNSTR = 'host=192.168.99.100 port=15432 dbname=netologydb user=postgres'


def create_db():  # create table
    # Password is provided by .pgpass

    with pg.connect(CONNSTR) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS student (
                    id serial PRIMARY KEY,
                    name varchar(100) not null,
                    gpa numeric(10,2),
                    birth timestamp with time zone
                )
                """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS course (
                    id serial PRIMARY KEY,
                    name varchar(100) not null
                )
                """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS student_course (
                    id serial PRIMARY KEY,
                    student_id bigint REFERENCES student(id),
                    course_id bigint REFERENCES course(id)
                )
                """)


def get_students(course_id):  # get students of the chosen course
    with pg.connect(CONNSTR) as conn:
        with conn.cursor() as cur:
            cur.execute("""      
                SELECT 
                    s.id, s.name, c.name
                FROM student AS s
                JOIN student_course AS sc
                    ON sc.student_id = s.id
                JOIN course AS c
                    ON c.id = %s
            """, (course_id, ))
            return cur.fetchall()


def _add_student(student, cursor):
    cursor.execute("""
       INSERT into student (name, gpa, birth) values (%s, %s, %s) 
       returning id 
       """, (student['name'], student['gpa'], student['birth']))
    return cursor.fetchone()[0]


def add_students(course_id, students):  # create students and write them into course table
    student_ids = []
    with pg.connect(CONNSTR) as conn:
        with conn.cursor() as cur:
            for student in students:
                student_ids.append(
                    _add_student(student, cur))
            for stud_id in student_ids:
                cur.execute("""
                    INSERT INTO 
                        student_course (student_id, course_id)
                    VALUES
                        (%s, %s)
                    """, (stud_id, course_id))


def add_student(student):  # just create student
    with pg.connect(CONNSTR) as conn:
        with conn.cursor() as cur:
            _add_student(student, cur)


def add_course(name):
    with pg.connect(CONNSTR) as conn:
        with conn.cursor() as cur:
            cur.execute("""
               INSERT into course (name) values (%s) 
               returning id 
               """, (name, ))
            return cur.fetchone()[0]


def get_student(student_id):
    with pg.connect(CONNSTR) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                select * from student where student.id = (%s);
                """, (student_id,))
            return cur.fetchall()


if __name__ == '__main__':
    create_db()
    add_student({'name': 'Katie', 'gpa': 8, 'birth': '1986-01-01'})
    add_student({'name': 'Lily', 'gpa': 7, 'birth': '1986-01-01'})
    add_course('french')
    get_students(1)
