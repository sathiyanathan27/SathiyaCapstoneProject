#from cgitb import text
from flask import Flask,render_template,request
import model 
app = Flask('__name__')


@app.route('/')
def view():
    return render_template('index.html')

@app.route('/recommend',methods=['POST'])
def recommend_top5():
    try:
        # Get username from form
        user_name = request.form['User Name'].strip().lower()
        print('User name =', user_name)



        # Generate recommendations
        top20_products = model.recommend_products(user_name)
        get_top5 = model.top5_products(top20_products)

        return render_template(
            'index.html',
            column_names=get_top5.columns.values,
            row_data=list(get_top5.values.tolist()),
            zip=zip,
            text='Recommended products',
            error=None
        )

    except Exception as e:
        print("Error:", str(e))  # Log error to console
        return render_template(
            'index.html',
            column_names=[],
            row_data=[],
            zip=zip,
            text=None,
            error= "Oops, something went wrong. Please try a different username"
        )

if __name__ == '__main__':
    app.debug=False

    app.run()