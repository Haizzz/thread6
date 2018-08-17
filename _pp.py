# this file simplifies multithreading
import threading


class ResultThread(threading.Thread):
    """
    A custom Thread that can return the value of the function 
    runned inside it
    """
    fx_output = None

    def run(self, *args, **kwargs):
        try:
            if self._target:
                self.fx_output = self._target(*self._args, **self._kwargs)
        finally:
            # Avoid a refcycle if the thread is running a function with
            # an argument that has a member that points to the thread.
            del self._target, self._args, self._kwargs


def threaded(func):
    """
    A decorator to run a function in a separate thread, this is useful
    when you want to do any IO operations (network request, prints, etc...)
    and want to do something else while waiting for it to finish.

    :param func: the function to run in a separate thread
    :param daemon: boolean whether or not the run as a daemon
    :return: whatever func returns
    :raises: whatever func raises
    """
    def wrapper(*args, **kwargs):
        thread = ResultThread(target=func)
        thread.start()
        thread.join()
        return thread.fx_output

    return wrapper
