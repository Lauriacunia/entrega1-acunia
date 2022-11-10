from post.models import Post
from django.contrib.auth.models import User

User(username='lau', password='user_pass1', email='lau@gmail.com').save()
User(username='mica', password='user_pass2', email='mica@gmail.com').save()
User(username='jose', password='user_pass3', email='jose@gmail.com').save()
user_1 = User.objects.get(username='lau')
user_2 = User.objects.get(username='mica')
user_3 = User.objects.get(username='jose')

Post(title='Salary of a SQL Data Engineer', content='Data Engineers have always had to be familiar with relational SQL databases, but with newer data analytics platforms that even offer data integration and machine learning via SQL, more and more Data Engineers are focusing on this programming language. Is this paying off?', author= user_1, thumbnail='images/1.jpeg').save()
Post(title='Top 5 reasons why developers love Rust programming language', content='Rust is one of the few modern languages that has found a place in the industry where programmers are able to create code that is used by actual businesses. Let’s take a look at the things that make coding in Rust so appealing to programmers.', author= user_2, thumbnail='images/2.png').save()
Post(title='My Top 8 VS Code Extensions', content='I recently gave a talk at Microsoft Ignite where I used Visual Studio Code. The most frequently asked question was what extensions are you using? So, in this post I will share my top 8 Visual Studio Code extensions.', author=user_3, thumbnail='images/3.png').save()
Post(title='Top 4 event-driven architecture patterns', content='Software systems keep evolving rapidly and the number of people using software also keeps increasing by a large margin every year. This leads to new patterns and tools being introduced to accommodate for those evolvements.', author=user_2, thumbnail='images/4.jpeg').save()
Post(title='All About React’s Proposed New use() Hook', content='A feature proposal from the React core team is causing some buzz in the React ecosystem, drawing both excitement for its new capabilities, as well as some concerns about how it’s going to be implemented. In this post, we’ll dig into what the new feature looks like, what problem it solves, and what the concerns are being raised.', author=user_2, thumbnail='images/5.jpeg').save()
Post(title='That’s why you need to understand class scopes in Python', content='Take a look at the below code and try to find out the value for each print() before checking the results. If you get them all right and completely understand why those are the right results, this article will not provide too much new information, otherwise I strongly encourage you to continue reading in order to understand the underlying concepts.', author=user_3, thumbnail='images/6.png').save()


print('📚 Se han creado algunos post iniciales ')