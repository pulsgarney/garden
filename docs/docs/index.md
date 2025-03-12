Introduction to Garden
====

## Overview

**Garden** is a straightforward asynchronous task management library for Python. It is ideal for all uncomplicated tasks that do not require a task dependency system. It performs exceptionally well for tasks that are simple and small in nature, asynchronous, require repetition or dispatching, and can pause when certain conditions are met. For instance, tasks such as data crawling and extractions.

## Requirements

  * Python 3.10+
  * No OS specific features required, should be working on all systems that supports Python.

## How it works

Garden is dependent on Python's inbuilt asynchronous module `asyncio` to universally create an event loop queue in the background. Through the exposure of a small number of APIs, it enables you to define tasks with a few parameters, and it will automatically manage the execution and handle errors gracefully. Additionally, it features middleware-based functionality, allowing you to add third-party features to your tasks without extensive development on the task itself.

It serves as a boilerplate solution for those who wish to commence asynchronous task programming in Python without having to comprehend an excessive amount of background knowledge. Having said that, since it employs asynchronous programming, you need to program your logic in accordance with the asynchronous programming paradigm. For instance, use the async/await syntax to define asynchronous logics, avoid blocking calls, or refrain from using it for any CPU-intensive tasks.

## Why Garden

While managing asynchronous programming in Python isn't overly difficult, handling complex asynchronous tasks can be quite challenging. Moreover, it can be extremely tedious to have to manually code most of the flow logic repeatedly in a multitude of similar tasks. Garden is designed to streamline this process by providing a straightforward interface for defining and executing asynchronous tasks.

Asyncio is a potent library for asynchronous programming in Python. Coroutines are more resource-efficient than threads. They are also easier to manage as they don't require a separate thread for each task or system-level context changes. It is well-suited for I/O-bound tasks like network requests or reading/writing to files.

I created this library mainly because I have numerous small tasks such as data processing and cleaning for my projects. For the most part, it isn't worthwhile to use a full-fledged framework for such simple tasks. That's why I developed Garden. It's like the minor daily work you do casually with the assistance of some little animal in the background. While building it, I drew some inspiration from React (the JavaScript library) in terms of lifecycle and state management to offer more control over the hooks and the non-linear flow of data management.
