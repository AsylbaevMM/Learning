def limiter(limit, unique, lookup):
    instances = {}

    def decorator(cls):

        def new_new(cls, *args, **kwargs):
            identifier = kwargs.get(unique)
            if identifier in instances:
                return instances[identifier]

            if len(instances) >= limit:
                if lookup == "FIRST":
                    return next(iter(instances.values()))
                elif lookup == "LAST":
                    return list(instances.values())[-1]

            instance = super().__new__(cls)
            instances[identifier] = instance
            return instance

        cls.__new__ = new_new
        return cls

    return decorator