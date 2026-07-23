'''
Case Study: Food Delivery Apllication
Imagine you're developing a Food Delivery App.
The Application can run in three env:
Development
Testing
Production
'''

#Define Config classes
class DevConfig:
    database = "sqlite.db"
    debug = True
class TestConfig:
    database = "test.db"
class ProdConfig:
    database="mysql://food_app"
    debug = False


#Step2: Define a config factory(Callable)
def get_config(environment):
    if environment == "dev":
        return DevConfig()
    elif environment == "test":
        return TestConfig()
    else:
        return ProdConfig()
    
#Step3: Use the factory
env = "dev"

config = get_config(env)

print(config.database)
print(config.debug)