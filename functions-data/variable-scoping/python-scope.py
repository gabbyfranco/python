#global scope
my_global = 10

def fn1():
    
    enclosed_v = 8
    
    def fn2():
        local_v = 5
        print('Access to Global', my_global)
        fn2()

fn1()

print(enclosed_v)
print(local_v)