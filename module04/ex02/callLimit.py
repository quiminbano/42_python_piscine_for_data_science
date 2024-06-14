def callLimit(limit: int):
    count = 0

    def callLimiter(function):
        def limit_function(*args, **kwargs):
            try:
                nonlocal count
                count += 1
                if count > limit:
                    raise Exception(f"Error: {function} call too many times")
                return function(*args, **kwargs)
            except Exception as e:
                print(e)
                return None
        return limit_function
    return callLimiter
