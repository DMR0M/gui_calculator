# Created package files using script
import flet as ft
import math
from pathlib import Path


# Main app function
def main(page: ft.page):
	page.title = 'PyCalculator'
	page.window_height = 450
	page.window_width = 350
	page.bgcolor = '#232323'

	# Button event handler
	def keyboard(e):
		try:
			data = e.control.data

			# Validate button input
			if (data in [str(n) for n in range(0, 10)]) or \
				(data in ['<', '.', '+', '-', '*', '/', '(', ')', '**']):
				txt.value = str(txt.value) + str(data)
				page.update()

			# Show result
			if data == '=':
				txt.value = str(eval(txt.value))
				page.update()

			# Remove digit
			if data == 'e':
				st = list(txt.value)
				st.pop()
				txt.value = ''.join(map(str, st))
				page.update()

			# Clear numbers or equation
			if data == 'C':
				st = list(txt.value)
				st.pop()
				txt.value = ''
				page.update()

			# Round off function
			if data == '≈':
				txt.value = round(int(txt.value))
				txt.value = str(txt.value)
				page.update()

			# Square root function
			if data == '√':
				txt.value = str(math.sqrt(int(txt.value)))
				page.update()

		except (ValueError, IndexError, SyntaxError):
			txt.value = 'Syntax Error'
			page.update()

	txt = ft.TextField(
		read_only=True,
		border_color='#FFFFFF',
		text_style=ft.TextStyle(size=30, color='#FFFFFF')
	)
	# Row 1: Buttons
	# <, (, ), ÷
	btn_e = ft.ElevatedButton(
		text='<', bgcolor='#FFB703', color='#FFFFFF', data='e', on_click=keyboard,
		style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
	)
	btn_po = ft.ElevatedButton(
		text='(', bgcolor='#FFB703', color='#FFFFFF', data='(', on_click=keyboard,
		style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
	)
	btn_pc = ft.ElevatedButton(
		text=')', bgcolor='#FFB703', color='#FFFFFF', data=')', on_click=keyboard,
		style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
	)
	btn_division = ft.ElevatedButton(
		text='÷', bgcolor='#2A93D5', color='#232323', data='/', on_click=keyboard,
		style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
	)

	r1 = ft.Row(
		controls=[btn_e, btn_po, btn_pc, btn_division],
		alignment=ft.MainAxisAlignment.SPACE_BETWEEN
	)

	# Row 2: Buttons
	# 7, 8, 9, *
	btn_7 = ft.ElevatedButton(
		text='7', bgcolor='#FFFFFF', color='#232323', data='7', on_click=keyboard,
		style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
	)
	btn_8 = ft.ElevatedButton(
		text='8', bgcolor='#FFFFFF', color='#232323', data='8', on_click=keyboard,
		style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
	)
	btn_9 = ft.ElevatedButton(
		text='9', bgcolor='#FFFFFF', color='#232323', data='9', on_click=keyboard,
		style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
	)
	btn_multiplication = ft.ElevatedButton(
		text='×', bgcolor='#2A93D5', color='#232323', data='*', on_click=keyboard,
		style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
	)

	r2 = ft.Row(
		controls=[btn_7, btn_8, btn_9, btn_multiplication],
		alignment=ft.MainAxisAlignment.SPACE_BETWEEN
	)

	# Row 3: Buttons
	# 4, 5, 6, -
	btn_4 = ft.ElevatedButton(
		text='4', bgcolor='#FFFFFF', color='#232323', data='4', on_click=keyboard,
		style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
	)
	btn_5 = ft.ElevatedButton(
		text='5', bgcolor='#FFFFFF', color='#232323', data='5', on_click=keyboard,
		style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
	)
	btn_6 = ft.ElevatedButton(
		text='6', bgcolor='#FFFFFF', color='#232323', data='6', on_click=keyboard,
		style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
	)
	btn_subtraction = ft.ElevatedButton(
		text='-', bgcolor='#2A93D5', color='#232323', data='-', on_click=keyboard,
		style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
	)

	r3 = ft.Row(
		controls=[btn_4, btn_5, btn_6, btn_subtraction],
		alignment=ft.MainAxisAlignment.SPACE_BETWEEN
	)

	# Row 4: Buttons
	# 1, 2, 3, +
	btn_1 = ft.ElevatedButton(
		text='1', bgcolor='#FFFFFF', color='#232323', data='1', on_click=keyboard,
		style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
	)
	btn_2 = ft.ElevatedButton(
		text='2', bgcolor='#FFFFFF', color='#232323', data='2', on_click=keyboard,
		style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
	)
	btn_3 = ft.ElevatedButton(
		text='3', bgcolor='#FFFFFF', color='#232323', data='3', on_click=keyboard,
		style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
	)
	btn_addition = ft.ElevatedButton(
		text='+', bgcolor='#2A93D5', color='#232323', data='+', on_click=keyboard,
		style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
	)

	r4 = ft.Row(
		controls=[btn_1, btn_2, btn_3, btn_addition],
		alignment=ft.MainAxisAlignment.SPACE_BETWEEN
	)

	# Row 5: Buttons
	# C, 0, ., =
	btn_c = ft.ElevatedButton(
		text='C', bgcolor='#FFFFFF', color='#232323', data='C', on_click=keyboard,
		style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
	)
	btn_0 = ft.ElevatedButton(
		text='0', bgcolor='#FFFFFF', color='#232323', data='0', on_click=keyboard,
		style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
	)
	btn_point = ft.ElevatedButton(
		text='.', bgcolor='#FFFFFF', color='#232323', data='.', on_click=keyboard,
		style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
	)
	btn_equal = ft.ElevatedButton(
		text='=', bgcolor='#2A93D5', color='#232323', data='=', on_click=keyboard,
		style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
	)

	r5 = ft.Row(
		controls=[btn_c, btn_0, btn_point, btn_equal],
		alignment=ft.MainAxisAlignment.SPACE_BETWEEN
	)

	# Row 6: Buttons
	# ≈, √, ^
	btn_round = ft.ElevatedButton(
		text='≈', bgcolor='#FFB703', color='#FFFFFF', data='≈', on_click=keyboard,
		style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
	)
	btn_root = ft.ElevatedButton(
		text='√', bgcolor='#FFB703', color='#FFFFFF', data='√', on_click=keyboard,
		style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
	)
	btn_exponent = ft.ElevatedButton(
		text='^', bgcolor='#FFB703', color='#FFFFFF', data='**', on_click=keyboard,
		style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
	)
	python_img = ft.Image(
		src=str(Path.cwd() / 'gui_app' / 'img' / 'snek_3.png'),
		width=65,
		height=50,
		fit=ft.ImageFit.CONTAIN,
	)

	r6 = ft.Row(
		controls=[btn_round, btn_root, btn_exponent, python_img],
		alignment=ft.MainAxisAlignment.SPACE_BETWEEN
	)

	# Adding the row of buttons in the GUI
	page.add(txt)
	page.add(
		r1,
		r2,
		r3,
		r4,
		r5,
		r6,
	)


ft.app(target=main)

