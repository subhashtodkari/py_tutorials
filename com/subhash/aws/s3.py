import boto3
import uuid

# low level api for more control
# - good performance but complex and less readable code
# generated from JSON service definition file
s3_client = boto3.client('s3')

# high level api - easy to use but limited operations and slightly less performance
# generated from JSON resource definition file
# get client from resource => s3_resource.meta.client
s3_resource = boto3.resource('s3')


# print all buckets and objects
def print_all_s3_objects():
    for b in s3_resource.buckets.all():
        print('bucket: ', b)
        for obj in b.objects.all():
            print('object: ', obj.key, obj.storage_class)


def generate_bucket_name(prefix):
    return ''.join([prefix, '-',  str(uuid.uuid4())])


def create_bucket(prefix, conn):
    print('creating a bucket...')
    session = boto3.session.Session()
    region = session.region_name
    name = generate_bucket_name(prefix)
    print('with name: ', name, ', region: ', region)
    resp = conn.create_bucket(Bucket=name
                              # don't specify region for 'us-east-1' - special case
                              # , CreateBucketConfiguration={'LocationConstraint': region}
                              )
    return name, resp


def delete_bucket(name, conn):
    print('Starting deletion of bucket: ', name)

    # delete all objects from bucket
    objs = []
    bucket = conn.Bucket(name)
    for obj in bucket.object_versions.all():
        objs.append({'Key': obj.object_key, 'VersionId': obj.version_id})

    print('Deleting objects: ', objs)
    if len(objs) > 0:
        bucket.delete_objects(Delete={'Objects': objs})

    print('Deleting bucket')
    bucket.delete()


def create_temp_file(file_name, file_content, size):
    random_name = ''.join([str(uuid.uuid4().hex[:6]), file_name])

    with open(random_name, 'w') as f:
        f.write(str(file_content) * size)

    print('created temp file: ', random_name)
    return random_name


def add_object_to_bucket(b_name, object_name, file, conn):
    print('bucket: ', b_name, ' >> adding object: ', object_name)
    conn.Bucket(b_name).Object(object_name).upload_file(file)


if __name__ == "__main__":

    # print all objects before changes
    print_all_s3_objects()

    # add bucket to s3
    bucket_name, resp = create_bucket('test', s3_resource)
    print('New bucket created: ', bucket_name)

    # add file to bucket
    random_file = create_temp_file('temp_file.txt', 'This is temp file', 5)
    print('Temp file created: ', random_file)
    add_object_to_bucket(bucket_name, 'sample file', random_file, s3_resource)

    # print all objects after addition of bucket and object to it
    print_all_s3_objects()

    # delete file object from bucket
    delete_bucket(bucket_name, s3_resource)
