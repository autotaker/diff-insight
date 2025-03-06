---
date: '2025-03-06'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:71adf7f...MicrosoftDocs:31c2d64
summary: この変更では、`latest-inference-preview.md`ファイルに軽微な更新が行われました。具体的には、「modalities」、「prediction」、「audio」プロパティの説明が改善され、ユーザーがAPI出力の種類や音声出力時のパラメータについて理解しやすくなりました。また、リンクも更新され、情報の正確性と最新性が向上しました。このリリースには特に破壊的な変更は含まれておらず、全体としてユーザー体験の向上と情報の透明性を意識した良い更新となっています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:71adf7f...MicrosoftDocs:31c2d64){target="_blank"}

# Highlights
この変更では、`latest-inference-preview.md`ファイルに対して軽微な更新が行われました。主に、「modalities」、「prediction」、「audio」プロパティに関する説明が改善され、これによりユーザーがAPI出力の種類や、音声出力時のパラメータについてより理解しやすくなっています。さらに、リンクの更新も行われ、情報の正確性と最新性が向上しました。

## New features
- API出力に関する説明が整理され、理解がしやすくなりました。
- リンクを更新し、より正確で最新の情報が提供されるようになりました。

## Breaking changes
- このリリースには特に破壊的な変更は含まれていません。

## Other updates
- 「modalities」、「prediction」、「audio」プロパティの説明が改善されました。

# Insights
この記事の更新は、主にAPIの使用に際してより詳細で明確な情報を提供することを目的としているようです。特に、`latest-inference-preview.md`では、ユーザーがどのような出力を期待できるかを理解しやすくするために、「modalities」や「prediction」、そして「audio」に関する情報が改善されています。これらのプロパティは、機械学習や人工知能において音声や異なるタイプの出力を扱う際に重要な概念です。

リンクの更新は、ユーザーが常に最新の情報にアクセスできるようにするためのものであり、これはAPI使用時のトラブルシューティングや、開発のヒントを得る際に非常に有用です。全体感じとしては、ユーザー体験の向上と情報の透明性を意識した良い更新といえます。

このように、今回の更新では特定のプロパティに焦点を当て、より実用的で直感的な指標を提供し、ユーザーがAIサービスを効率的に活用できるようにしています。このことは、開発者だけでなく、ビジネスユースや研究者にとっても業務効率化を促進するものです。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [latest-inference-preview.md](#item-24bf0f) | minor update | API バージョンの最新予測プレビューの情報更新 | modified | 3 | 3 | 6 | 


# Modified Contents
## articles/ai-services/openai/includes/api-versions/latest-inference-preview.md{#item-24bf0f}

<details>
<summary>Diff</summary>
````diff
@@ -4657,9 +4657,9 @@ Represents a completion response from the API. Note: both the streamed and non-s
 | function_call | string or [chatCompletionFunctionCallOption](#chatcompletionfunctioncalloption) | Deprecated in favor of `tool_choice`.<br><br>Controls which (if any) function is called by the model.<br>`none` means the model won't call a function and instead generates a message.<br>`auto` means the model can pick between generating a message or calling a function.<br>Specifying a particular function via `{"name": "my_function"}` forces the model to call that function.<br><br>`none` is the default when no functions are present. `auto` is the default if functions are present.<br> | No |  |
 | functions | array | Deprecated in favor of `tools`.<br><br>A list of functions the model may generate JSON inputs for.<br> | No |  |
 | user_security_context | [userSecurityContext](#usersecuritycontext) | User security context contains several parameters that describe the AI application itself, and the end user that interacts with the AI application. These fields assist your security operations teams to investigate and mitigate security incidents by providing a comprehensive approach to protecting your AI applications. [Learn more](https://aka.ms/TP4AI/Documentation/EndUserContext) about protecting AI applications using Microsoft Defender for Cloud. | No |  | and detect abuse.<br> | No |  |
-| modalities | [ChatCompletionModalities](#chatcompletionmodalities) | Output types that you would like the model to generate for this request.<br>Most models are capable of generating text, which is the default:<br><br>`["text"]`<br><br>The `gpt-4o-audio-preview` model can also be used to [generate audio](/docs/guides/audio). To<br>request that this model generate both text and audio responses, you can<br>use:<br><br>`["text", "audio"]`<br> | No |  |
-| prediction | [PredictionContent](#predictioncontent) | Configuration for a [Predicted Output](/docs/guides/predicted-outputs), which can greatly improve response times when large parts of the model response are known ahead of time. This is most common when you are regenerating a file with only minor changes to most of the content. | No |  |
-| audio | object | Parameters for audio output. Required when audio output is requested with<br>`modalities: ["audio"]`. [Learn more](/docs/guides/audio).<br> | No |  |
+| modalities | [ChatCompletionModalities](#chatcompletionmodalities) | Output types that you would like the model to generate for this request.<br>Most models are capable of generating text, which is the default:<br><br>`["text"]`<br><br>The `gpt-4o-audio-preview` model can also be used to [generate audio](/azure/ai-services/openai/realtime-audio-quickstart). To<br>request that this model generate both text and audio responses, you can<br>use:<br><br>`["text", "audio"]`<br> | No |  |
+| prediction | [PredictionContent](#predictioncontent) | Configuration for a [Predicted Output](/azure/ai-services/openai/how-to/predicted-outputs), which can greatly improve response times when large parts of the model response are known ahead of time. This is most common when you are regenerating a file with only minor changes to most of the content. | No |  |
+| audio | object | Parameters for audio output. Required when audio output is requested with<br>`modalities: ["audio"]`. [Learn more](/azure/ai-services/openai/realtime-audio-quickstart).<br> | No |  |
 
 ### Properties for audio
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "API バージョンの最新予測プレビューの情報更新"
}
```

### Explanation
この修正では、`latest-inference-preview.md`というファイルに対していくつかの軽微な更新が行われました。具体的には、APIの出力に関する情報を整理し、特に「modalities」や「prediction」、「audio」というプロパティの説明が改善されています。これにより、どのような出力が可能であるか、また音声出力が要求された際のパラメータについての理解が向上します。修正内容には、リンクの更新も含まれており、より正確で最新の情報提供を目指しています。全体として、ユーザーにとって有益な内容の改訂が進められています。


