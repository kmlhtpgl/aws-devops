from flask import Flask, render_template, request

app = Flask(__name__)


def convertMillis(number):
     seconds=(number/1000)%60
     minutes=(number/(1000*60))%60
     hours=(number/(1000*60*60))
     return seconds, minutes, hours

def main(number):
    con_sec, con_min, con_hour = convertMillis(int(number))
    split_sec = str(con_sec).split('.')
    int_sec = int(split_sec[0])
    split_min = str(con_min).split('.')
    int_min = int(split_min[0])
    split_hour = str(con_hour).split('.')
    int_hour = int(split_hour[0])
    converted = ''
    if int(number) < 1000:
        converted = str(number) + ' milliseconds'
        return converted 
        #print(f"just {millis} milliseconds")
    elif int(number) >= 1000 and int(number) < 60000:
        converted = str(int_sec) + ' second/s'
        return converted
        #print(f"{int_sec} second/s")
    elif int(number) >= 60000 and int(number) < 3600000:
        converted = str(int_min) + ' minute/s' + ' ' + str(int_sec) + ' second/s'
        return converted
        #print(f"{int_min} minute/s {int_sec} second/s")
    else:
        converted = str(int_hour) + ' hour/s' + ' ' + str(int_min) + ' minute/s' + ' ' + str(int_sec) + ' second/s'
        return converted
        #print(f"{int_hour} hour/s {int_min} minute/s {int_sec} second/s")  
                    
 


@app.route('/', methods=['POST', 'GET'])

def main_post():
    if request.method == 'POST':
        alpha = request.form['number']
        if not alpha.isdecimal():
            return render_template('index.html', not_valid = True, developer_name = 'Kemal')
        number = int(alpha)
        if  not number > 0:
            return render_template('index.html', not_valid = True, developer_name = 'Kemal')
        
        return render_template('result.html', not_valid = False, developer_name = 'Kemal', milliseconds = number, result = main(number))

    
    else:
        return render_template('index.html', not_valid = False, developer_name = 'Kemal')
if __name__ == '__main__':
    app.run(debug=True)

