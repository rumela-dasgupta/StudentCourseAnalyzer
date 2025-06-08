import sys
import csv
from pyhtml import html,head, title, body, h1, table, tr, td, th, style, img
import matplotlib.pyplot as plt

print(sys.argv)

# Checking arguments
if len(sys.argv) != 3:
    message = html(
        head(title("Something Went Wrong")),
        body(h1("Wrong Inputs"), "Something went wrong")
    )
    with open("output.html", "w") as f:
        f.write("<!DOCTYPE html>\n" + str(message))
    sys.exit()

mode = sys.argv[1]   # either '-s' or '-c'
id_value = sys.argv[2]  # string like '101' or '201'
data = []
try:
    f = open("data.csv", "r", encoding='latin1')
    reader = csv.reader(f)
    next(reader)  # Skip header row
    for i in reader:
        data.append(i)  # row = [student_id, course_id, marks]
    f.close()
except FileNotFoundError:
    print("data not found")
    f.close()

# student mode
total_marks = 0
if mode == '-s':
    student_rows = []
    for i in data:
       if len(i) >= 3 and i[0] == id_value:
         student_rows.append(i)
         total_marks += int(i[2])

    if student_rows == []:
        error_page = html(
            head(title("Something Went Wrong")),
            body(h1("Wrong Inputs"), "Something went wrong")
        )
        with open("output.html", "w") as f:
            f.write("<!DOCTYPE html>\n" + str(error_page))
        sys.exit()

    # HTML table generation
    rows = [tr(th("Student id"), th("Course id"), th("Marks"))]
    for r in student_rows:
        rows.append(tr(td(r[0]), td(r[1]), td(r[2])))
    rows.append(tr(td(""), td("Total Marks"), td(str(total_marks))))

    student_html = html(
        head(
            title("Student Data"),
            style("""
                table {
                    border: 1px solid black;
                    border-collapse: collapse;
                }
                th, td {
                    border: 1px solid black;
                    padding: 4px;
                    
                }
                tr:last-child td:nth-child(2) {
                    padding-left: ;
                    font-weight: ;
                }
            """)
        ),
        body(
            h1("Student Details"),
            table(*rows)
        )
    )
    with open("output.html", "w", encoding="utf-8") as f:
        f.write("<!DOCTYPE html>\n" + str(student_html))


# course mode
if mode == '-c':
    course_rows = []
    for i in data:
        if len(i) >= 3 and i[1] == id_value:
            course_rows.append(i)

    if course_rows == []:
        error_page = html(
            head(title("Something Went Wrong")),
            body(h1("Wrong Inputs"), "Something went wrong")
        )
        with open("output.html", "w") as f:
            f.write("<!DOCTYPE html>\n" + str(error_page))
        sys.exit()

    marks = [int(row[2]) for row in course_rows]
    avg_marks = sum(marks) / len(marks)
    max_marks = max(marks)
    plt.hist(marks)
    plt.xlabel("Marks")
    plt.ylabel("Frequency")
    plt.savefig("histogram.png")
    plt.close()

    rows = [tr(th("Average Marks"), th("Maximum Marks"))]
    rows.append(tr(td(str(avg_marks)), td(str(max_marks))))
    course_html = html(
    head(
        title("Course Data"),
        style("""
            table {
                border: 1px solid black;
                border-collapse: collapse;
            }
            th, td {
                border: 1px solid black;
                padding: 4px;
            }
            tr:last-child td:nth-child(2) {
                padding-left: ;
                font-weight: ;
            }
        """)
    ),
    body(
        h1("Course Details"),
        table(*rows),
        img(src="histogram.png", alt="Histogram of Marks")
    )
)

    
    with open("output.html", "w", encoding="utf-8") as f:
        f.write("<!DOCTYPE html>\n" + str(course_html))
