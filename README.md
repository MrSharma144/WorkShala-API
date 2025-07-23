# WorkShala-API

This is a Django-based API project, configured for deployment on [Vercel](https://vercel.com/).

## Features

- Django REST API backend
- Ready for serverless deployment on Vercel
- Python 3.9 compatibility

## Project Structure

```
django_api/
├── django_api/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── manage.py
├── vercel.json
```

## Deployment on Vercel

1. **Install dependencies**

   Make sure you have a `requirements.txt` file with all your Python dependencies.

   ```sh
   pip install -r requirements.txt
   ```

2. **Vercel Configuration**

   The `vercel.json` file is already set up to use your Django WSGI app as a serverless function:

   ```json
   {
     "version": 2,
     "builds": [
       {
         "src": "django_api/wsgi.py",
         "use": "@vercel/python",
         "config": {
           "maxLambdaSize": "50mb",
           "runtime": "python3.9"
         }
       }
     ],
     "routes": [
       {
         "src": "/(.*)",
         "dest": "django_api/wsgi.py"
       }
     ]
   }
   ```

3. **Prepare for Vercel**

   - Ensure your `wsgi.py` exposes `app` as the callable (already done):

     ```python
     app = application  # For Vercel compatibility
     ```

   - Add any environment variables (such as `DJANGO_SECRET_KEY`, database URLs, etc.) in the Vercel dashboard.

4. **Deploy**

   - Install [Vercel CLI](https://vercel.com/download):

     ```sh
     npm i -g vercel
     ```

   - Deploy:

     ```sh
     vercel --prod
     ```

## Local Development

1. **Run migrations**

   ```sh
   python manage.py migrate
   ```

2. **Start the development server**

   ```sh
   python manage.py runserver
   ```

## Environment Variables

Set the following environment variables in your Vercel dashboard or a `.env` file for local development:

- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG`
- `DATABASE_URL` (if using a cloud database)

## License

MIT

---

**Made with Django & Vercel**