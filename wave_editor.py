import wave_helper as helper
import math

SAMPLE_RATE = 2000
MAX_VOLUME = 32767
MIN_VOLUME = -32768
START_MSG = """
        1.Change wav file
        2.Compose a melody
        3.Exit/Quit

        Please, choose what you would like to do: """
CHANGE_WAVE_MSG = """
        1.Would you like to reverse the audio file?
        2.Would you like to negate the audio file?
        3.Would you like to increase the speed of the audio file?
        4.Would you like to decrease the speed of the audio file?
        5.Would you like to increase the volume of the audio file?
        6.Would you like to decrease the volume of the audio file?
        7.Would you like to mute the volume of the audio file?
        8.Exit/Quit
        How would you like to change the wav file? """


def reverse_audio(audio_data):
    """
    this function returns the reversed order of a nested list
    and the list is the interpretation of a given wav file
    :param audio_data: a nested list
    :return:the reversed order of a nested list
    """
    return audio_data[::-1]


def audio_negation(audio_data):
    """
    this function returns the negative of every element in a nested list
    and the list is the interpretation of a given wav file
    :param audio_data: a nested list
    :return:a nested list where every element in the list is negated
    """
    for i in range(len(audio_data)):
        for j in range(len(audio_data[i])):
            audio_data[i][j] = int(-1 * audio_data[i][j])
            if audio_data[i][j] > MAX_VOLUME:
                audio_data[i][j] = MAX_VOLUME
            if audio_data[i][j] < MIN_VOLUME:
                audio_data[i][j] = MIN_VOLUME
    return audio_data


def increase_speed(audio_data):
    """
    this function returns a list the odd number list deleted from the nested list
    and the list is the interpretation of a given wav file
    :param audio_data: a nested list
    :return:a list the odd number list deleted from the nested list

    """
    return [even for i, even in enumerate(audio_data) if i % 2 == 0]


def decrease_speed(audio_data):
    """
    this function returns a nested list with the addition of list, which are the average of two list from the original list
    and the list is the interpretation of a given wav file
    :param audio_data: a nested list
    :return:a nested list with the addition of a list which is the average of two list from the original list

    """
    new_audio_data = []
    for i in range(len(audio_data)):
        lst = []
        if i != len(audio_data) - 1:
            new_audio_data.append(audio_data[i])
            for j in range(len(audio_data[i])):
                lst.append(int((audio_data[i][j] + audio_data[i + 1][j]) / 2))
            new_audio_data.append(lst)
        else:
            new_audio_data.append(audio_data[i])
    return new_audio_data


def volume_increase(audio_data):
    """
     this function returns the nested lists, where it's elements are multiplied by 1.2
     and the list is the interpretation of a given wav file
     :param audio_data: a nested list
     :return:a nested lists, where it's elements are multiplied by 1.2
     """
    for i in range(len(audio_data)):
        for j in range(len(audio_data[i])):
            audio_data[i][j] = int(1.2 * (audio_data[i][j]))
            if audio_data[i][j] > MAX_VOLUME:
                audio_data[i][j] = MAX_VOLUME
            if audio_data[i][j] < MIN_VOLUME:
                audio_data[i][j] = MIN_VOLUME
    return audio_data


def volume_decrease(audio_data):
    """
     this function returns the nested lists, where it's elements are divided by 1.2
     and the list is the interpretation of a given wav file
     :param audio_data: a nested list
     :return:a nested lists, where it's elements are divided by 1.2
     """
    for i in range(len(audio_data)):
        for j in range(len(audio_data[i])):
            audio_data[i][j] = int((audio_data[i][j]) / 1.2)
            if audio_data[i][j] > MAX_VOLUME:
                audio_data[i][j] = MAX_VOLUME
            if audio_data[i][j] < MIN_VOLUME:
                audio_data[i][j] = MIN_VOLUME
    return audio_data


def muting_filter(audio_data):
    """
    this function returns a nested list with the addition of lists, which are the averages of three consecutive lists
    and if there is not list before that function it only does the average of two consecutive lists
    and the list is the interpretation of a given wav file
    :param audio_data: a nested list
    :return:a nested list with the addition of lists, which are the averages of three consecutive lists
    and if there is not list before that function it only does the average of two consecutive lists

    """
    new_audio_data = []
    for i in range(len(audio_data)):
        if i == 0:
            lst = []
            for j in range(len(audio_data[i])):
                lst.append(int((audio_data[i][j] + audio_data[i + 1][j]) / 2))
            new_audio_data.append(lst)
        elif i == len(audio_data) - 1:
            lst = []
            for j in range(len(audio_data[i])):
                lst.append(int((audio_data[i][j] + audio_data[i - 1][j]) / 2))
            new_audio_data.append(lst)
        else:
            lst = []
            for j in range(len(audio_data[i])):
                lst.append(int((audio_data[i][j] + audio_data[i - 1][j] + audio_data[i + 1][j]) / 3))
            new_audio_data.append(lst)
    return new_audio_data


def open_melody_file(filename):
    """
    this function returns a nested list, which each list consists of a musical note and a digit
    :param filename: a name of a file
    :return: a nested list, which each list consists of a musical note and a digit
    """
    file_content = open(filename)
    result = [line.replace('\n', ' ') for line in file_content.readlines()]
    string = ''
    string = string.join(result)
    lst = string.split(' ')
    music_notes = []
    msc = ''
    for i in lst:
        if i.isalpha():
            msc = i
        if i.isdigit():
            let = i
            lst = [msc, int(let)]
            music_notes.append(lst)
    return music_notes


def frequency_converter(music_notes):
    """
    this function returns the musical note into it's corresponding frequency value
    :param music_notes: a nested list
    :return:the musical note into it's corresponding frequency value
    """
    for i in range(len(music_notes)):
        if music_notes[i][0] == "A":
            music_notes[i][0] = 440
        elif music_notes[i][0] == "B":
            music_notes[i][0] = 494
        elif music_notes[i][0] == "C":
            music_notes[i][0] = 523
        elif music_notes[i][0] == "D":
            music_notes[i][0] = 587
        elif music_notes[i][0] == "E":
            music_notes[i][0] = 659
        elif music_notes[i][0] == "F":
            music_notes[i][0] = 698
        elif music_notes[i][0] == "G":
            music_notes[i][0] = 784
        elif music_notes[i][0] == "Q":
            music_notes[i][0] = 0
    return music_notes


def note_composer(sample_rate, note):
    """
    this function returns the calculation of the sample
    :param sample_rate: a constant
    :param note: the musical note
    :return: returns the calculation of the sample
    """
    lst = []
    n = int((sample_rate / 16) * note[1])
    if note[0] == 0:
        for i in range(n):
            lst.append([0,0])
    else:
        samples_per_cycle = sample_rate / note[0]
        for i in range(n):
            x = MAX_VOLUME * math.sin(math.pi * 2 * i / samples_per_cycle)
            x = int(x)
            lst.append([x, x])
    return lst


def exit_menu(frame_rate, audio_data):
    """
    this function creates a new file with all your made changes and asks you to give it a names it
    and then returns you to the main menu
    :param frame_rate: sample_rate
    :param audio_data: a nested list
    :return: to the main menu
    """
    wave_filename = input('Please, choose the name of your new file: ')
    helper.save_wave(frame_rate, audio_data, wave_filename)
    return main_menu()


def composing_melody():
    """
    this function takes an input,which is a text file, which turns the contents of the file to a  list which
    contain lists of  letters and number.
    """
    filename = input('Please, choose the name of the composition file!')
    melody = open_melody_file(filename)
    melody = frequency_converter(melody)
    audio_data = []
    for i in range(len(melody)):
        audio_data.extend(note_composer(SAMPLE_RATE, melody[i]))
    change_wave(SAMPLE_RATE, audio_data)

def change_wave(frame_rate, audio_data):
    """
    this function takes an input, which are eight changes to nested list or composition
    :param frame_rate: a constant
    :param audio_data: a nested list
    :return: the function it's self
    """
    user_input = True
    while user_input:
        user_input = input(CHANGE_WAVE_MSG)
        if user_input == "1":
            audio_data = reverse_audio(audio_data)
        elif user_input == "2":
            audio_data = audio_negation(audio_data)
        elif user_input == "3":
            audio_data = increase_speed(audio_data)
        elif user_input == "4":
            audio_data = decrease_speed(audio_data)
        elif user_input == "5":
            audio_data = volume_increase(audio_data)
        elif user_input == '6':
            audio_data = volume_decrease(audio_data)
        elif user_input == "7":
            audio_data = muting_filter(audio_data)
        elif user_input == "8":
            exit_menu(frame_rate, audio_data)
            break
        else:
            print('''
                                invalid input  ''')
            return change_wave(frame_rate, audio_data)
    return


def main_menu():
    """
    this function is the main function where it everything is put together ,where it asks the user what he wanted to pick
    :return: returns the picked input
    """
    user_input = input(START_MSG)
    if user_input == '1':
        audio_input = input("Please, enter the name of the file that you want to change:")
        frame_rate, audio_data = helper.load_wave(audio_input)
        change_wave(frame_rate, audio_data)
    elif user_input == "2":
        composing_melody()
    elif user_input == '3':
        return
    else:
        print('''
                    invalid input  ''')
        return main_menu()
if __name__ == '__main__':
    main_menu()