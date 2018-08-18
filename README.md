# \_pp (\_ parallel processing)
Simple parallel processing interface for python

## Why?
Python's built in parallel processing and threading library is pretty simple to implement but sometimes you just want to chuck data at a function and make it run faster

## Requirements
Python 3+

## Installation

## Quickstart
Use the `threaded` decorator to turn a method into a threaded method. That's it!
```python
@_pp.threaded()
def threaded_print():
    print("")
    return 1
```

Alternatively, use `run_threaded` function
```python
_pp.run_threaded(threaded_print)
```

Both the `threaded` decorator and `run_threaded` method will return an instance of
`ResultThread`. This allow you to optionally wait for the function to finish executing 
and get the return value. To get the return value, use `.await_output()`
```python
result = threaded_print()
result.await_output()  # this will return 1
```

If you have a function that needs to execute on a large list of data, use `run_chunked`
```python
def update_items(items):
    ...

items = [...]
run_chunked(update_items, items)
```
`.await_output()` also work with `run_chunked` but will return a list of return values instead

## Usage


## Todo
- [x] threaded function decorator
- [x] run something in a separate thread function
- [x] split data into chunk and run in separate threads
- [ ] add way for errors to fail loudly
- [ ] auto spawn to run fx on a set of data
- [ ] explore multi processing?
