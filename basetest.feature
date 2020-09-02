Feature: PadSplit staging website

	Scenario: We are visiting the PadSplit staging website
		Given we are on the PadSplit staging website
			Then the site title should read "Home | PadSplit"

	Scenario: We need to create a PadSplit account
		Given we are on the PadSplit staging website
			When we click the get started button
			Then the sign up dialog should appear
		Given the sign up form is open
			When we fill out the member sign up form
			And click the age certification
			And click the get started form button
			Then we should be redirected to user home page

	Scenario: We need to log out of a PadSplit account
		Given we are signed into a PadSplit account
			When we click the log out button
			Then we should be logged out

	Scenario: We need to log in to a PadSplit account
		Given we are on the PadSplit staging website
			When we click the sign in button
			Then the sign in dialog should appear
		Given the sign in form is open
			When we fill out the sign in form
			And click the sign in form button
			Then we should be signed in

