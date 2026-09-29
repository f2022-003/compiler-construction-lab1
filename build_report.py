"""Build the Lab-410 Task 1 submission document (docx)."""
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

doc = Document()

style = doc.styles["Normal"]
style.font.name = "Calibri"
style.font.size = Pt(11)

# Title block
t = doc.add_paragraph()
t.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = t.add_run("Lab-410 — Compiler Construction Lab")
r.bold = True
r.font.size = Pt(16)

t = doc.add_paragraph()
t.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = t.add_run("Task 1: Compiler vs Interpreter — Time Comparison")
r.bold = True
r.font.size = Pt(13)

t = doc.add_paragraph()
t.alignment = WD_ALIGN_PARAGRAPH.CENTER
t.add_run("Fall 2026  |  CLO1").font.size = Pt(11)

doc.add_paragraph()

info = doc.add_paragraph()
info.add_run("Name: ").bold = True
info.add_run("Usman hassan")
info = doc.add_paragraph()
info.add_run("Enrollment No: ").bold = True
info.add_run("f2022-003")

# Goal
doc.add_heading("Goal", level=1)
doc.add_paragraph(
    "Compare how long a compiled language (C++) and an interpreted language (Python) "
    "take to produce output for the same task, measuring compilation and execution "
    "separately for C++ and execution only for Python."
)

# Method
doc.add_heading("Method", level=1)
doc.add_paragraph(
    "For each C++ program, compilation time and execution time were measured separately "
    "with the time command; for each Python program only the total run time was measured. "
    "The real (wall-clock) value was recorded in every case."
)
cmds = [
    "time g++ sumA.cpp -o sumA     # compilation time",
    "time ./sumA                    # execution time",
    "time python3 sumA.py           # python total time",
]
for c in cmds:
    p = doc.add_paragraph()
    run = p.add_run(c)
    run.font.name = "Consolas"
    run.font.size = Pt(10)
doc.add_paragraph("The same three steps were repeated for fibB, primesC and sortD.")

# Results table
doc.add_heading("Results", level=1)
doc.add_paragraph(
    "Measured on Linux (g++ 13.3, Python 3.12). Outputs were verified identical "
    "across both languages: A → 4999999950000000, B → 9227465, C → 17984, "
    "D → correctly sorted array (min/max pair)."
)

headers = ["Program", "g++ compile time (real)", "C++ execution time (real)",
           "C++ total", "Python total (real)"]
rows = [
    ["A — Sum loop", "0.652s", "0.105s", "0.757s", "9.887s"],
    ["B — Recursion", "0.350s", "0.086s", "0.436s", "1.691s"],
    ["C — Conditionals", "0.394s", "0.027s", "0.421s", "1.083s"],
    ["D — Sorting", "0.544s", "0.216s", "0.760s", "2.457s"],
]
table = doc.add_table(rows=1 + len(rows), cols=len(headers))
table.style = "Light Grid Accent 1"
table.alignment = WD_TABLE_ALIGNMENT.CENTER
for i, h in enumerate(headers):
    cell = table.rows[0].cells[i]
    cell.text = ""
    run = cell.paragraphs[0].add_run(h)
    run.bold = True
    run.font.size = Pt(10)
for ri, row in enumerate(rows, start=1):
    for ci, val in enumerate(row):
        cell = table.rows[ri].cells[ci]
        cell.text = ""
        run = cell.paragraphs[0].add_run(val)
        run.font.size = Pt(10)

# Reflection
doc.add_heading("Reflection Questions", level=1)

q1 = doc.add_paragraph()
q1.add_run("1. Was C++'s total time always higher or lower than Python's? "
           "Was this consistent across all four programs?").bold = True
doc.add_paragraph(
    "C++'s total time was lower than Python's in all four programs — the result was "
    "fully consistent. Python ranged from about 2.6× slower (program C: 1.083s vs "
    "0.421s) to about 13× slower (program A: 9.887s vs 0.757s) than C++'s total."
)

q2 = doc.add_paragraph()
q2.add_run("2. Did compilation time change much between programs, or did it stay "
           "roughly the same regardless of what the program computes?").bold = True
doc.add_paragraph(
    "It stayed roughly the same (0.350s–0.652s). Compilation time depends on source "
    "size and the headers included (<iostream>, <vector>), not on the workload the "
    "program performs at run time — and all four sources are small, so g++ took a "
    "similar amount of time for each."
)

q3 = doc.add_paragraph()
q3.add_run("3. If you were going to run the same program 100 times, would you expect "
           "C++ or Python to save you more total time overall? Why?").bold = True
doc.add_paragraph(
    "C++, by a large margin. Compilation is a one-time cost; every additional run "
    "pays only the execution time. For program A, 100 runs cost C++ about "
    "0.652 + 100 × 0.105 ≈ 11.2s but cost Python 100 × 9.887 ≈ 989s. Because the "
    "compiled binary runs roughly 94× faster per run here, the gap widens with "
    "every repetition."
)

q4 = doc.add_paragraph()
q4.add_run("4. Based on your results, in what kind of situation would you prefer a "
           "compiled language, and in what situation would you prefer an interpreted "
           "language?").bold = True
doc.add_paragraph(
    "A compiled language (C++) is preferable for performance-critical or repeatedly "
    "executed code — heavy computation, tight loops, and production systems where "
    "run-time speed matters. An interpreted language (Python) is preferable for "
    "one-off scripts, prototyping, and exploratory work, where development speed "
    "matters more than execution speed and the edit–run cycle has no compile step."
)

doc.add_heading("Conclusion", level=1)
doc.add_paragraph(
    "The measurements confirm the practical difference between compilation and "
    "interpretation: C++ pays a small, roughly constant, one-time compilation cost "
    "and then executes far faster than Python, which re-interprets the code on "
    "every run. For repeated or compute-heavy work the compiled program wins "
    "decisively; for quick, write-and-run tasks the interpreted workflow is more "
    "convenient."
)

out = "/home/hatch/workspace/lab410-task1/Lab410_Task1_Report_f2022-003.docx"
doc.save(out)
print("saved", out)
