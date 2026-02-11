import pass_generator
import signal, sys

def signal_handler(sig, frame):
    print('\nprogram closed')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGQUIT, signal_handler)

if __name__ == '__main__':
    while True:
        try:
            _size:int = int(input("Size(>9): ")) 
            _word:str = pass_generator.generator(_size)
            print(f'Pass: {_word}')
            break
        except Exception as ex:
            print("You've pass any args wrongly, try again please!")
