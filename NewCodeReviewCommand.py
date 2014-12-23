import sublime
import sublime_plugin

class NewCodeReviewCommand(sublime_plugin.WindowCommand):
	def run(self):
		print("Starting New Code Review command...")

		self.pbiNumber = ""
		self.pbiTitle = ""

		#
		# Ask for PBI number and title
		#
		self.window.show_input_panel("PBI #", "", self.pbiInputOnDone, None, None)

	def pbiInputOnDone(self, input):
		print("User entered %s forr PBI" % (input,))
		self.pbiNumber = input

		self.window.show_input_panel("PBI Title", "", self.titleInputOnDone, None, None)

	def titleInputOnDone(self, input):
		print("User entered %s for title" % (input,))
		self.pbiTitle = input

		buffer = self.window.new_file()
		buffer.run_command("new_code_review_text", {
			"pbiNumber": self.pbiNumber,
			"pbiTitle": self.pbiTitle
		})

class NewCodeReviewTextCommand(sublime_plugin.TextCommand):
	def run(self, edit, pbiNumber, pbiTitle):
		template = """# Code Review of %s - %s

* """ % (pbiNumber, pbiTitle,)

		self.view.insert(edit, 0, template)
