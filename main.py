from plyer import notification

notification.notify(
    title="Notification Title",
    message="This is your notification message.",
    app_name="Your App Name",
    timeout=10  # Duration in seconds
)

exit()
from win10toast import ToastNotifier

# Create a ToastNotifier object
toaster = ToastNotifier()

# Show a notification
toaster.show_toast(
    "Notification Title",
    "Your message goes here!",
    duration=10,  # Duration in seconds
    icon_path=None  # You can provide a path to an .ico file
)
