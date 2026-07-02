'use strict';

// Dialogflow ES inline editor uses Cloud Functions gen 1.
// Keep this export name unchanged unless you also update the webhook function name.
const functions = require('firebase-functions/v1');

exports.dialogflowFirebaseFulfillment = functions.https.onRequest((request, response) => {
  if (request.method === 'GET') {
    response.status(200).send('Dialogflow fulfillment webhook is running.');
    return;
  }

  const body = request.body || {};
  const queryResult = body.queryResult || {};
  const intentName = queryResult.intent && queryResult.intent.displayName;

  console.log('Dialogflow intent:', intentName);
  console.log('Dialogflow parameters:', JSON.stringify(queryResult.parameters || {}));

  const intentMap = {
    'Default Welcome Intent': welcome,
    'Default Fallback Intent': fallback,

    // Add your own intents here. The key must exactly match the intent name in Dialogflow.
    // 'Your Intent Name': yourIntentHandler,
  };

  const handler = intentMap[intentName] || fallback;

  const result = handler(queryResult, body);
  response.json(result);
});

function welcome() {
  return textResponse('Welcome to my agent!');
}

function fallback() {
  return textResponse("I didn't understand. Can you try again?");
}

// Example custom handler for students:
//
// function yourIntentHandler(queryResult) {
//   const name = queryResult.parameters.name || 'there';
//   return textResponse('Hello ' + name + ', this response came from the inline editor.');
// }

function textResponse(message) {
  return {
    fulfillmentText: message,
    fulfillmentMessages: [
      {
        text: {
          text: [message],
        },
      },
    ],
  };
}
