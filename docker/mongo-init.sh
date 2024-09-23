set -e

mongosh -u="$MONGO_INITDB_ROOT_USERNAME" -p="$MONGO_INITDB_ROOT_PASSWORD" <<EOF
db = db.getSiblingDB('blog')

db.createUser({
  user: '$BLOG_USER',
  pwd: '$BLOG_PASSWORD',
  roles: [{ role: 'readWrite', db: 'blog' }],
});
db.createCollection('posts')
db.createCollection('authors')

EOF
