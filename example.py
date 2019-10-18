import coffeehouse

api_key = "b6aab00cbdebd95ab8f142e0941b5a8d152c9ad1f0a7f6312e81603719c6ca60359ff4f3"
api_client = coffeehouse.API(api_key)

session = api_client.create_session()
print("Session ID: {0}".format(session.id))
print("Session Available: {0}".format(str(session.available)))
print("Session Language: {0}".format(str(session.language)))
print("Session Expires: {0}".format(str(session.expires)))

while(True):
    output = session.think_thought(input("Input: "))
    print("Output: {0}".format(output))


# In the case you want to save the Session ID to reuse the session
# Use api_client to invoke think_thought instead, for example;
#
# while(True):
#     output = api_client.think_thought(session.id, input("Input: "))
#     print("Output: {0}".format(output))
#
# This is the same effect as above but uses the client directly.
