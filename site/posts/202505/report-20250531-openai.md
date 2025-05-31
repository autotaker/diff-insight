---
date: '2025-05-31'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:768223a...MicrosoftDocs:ca0291a
summary: この差分では、「code-interpreter.md」ファイルにおいて、Code Interpreterセッションのタイムアウトに関する情報が追加され、セッション管理が明確化されました。新機能として、Code
  Interpreterセッションがデフォルトで1時間アクティブであり、30分間のアイドルタイムアウトが存在することが示されています。特に破壊的な変更はなく、主に情報の追加と明確化に留まっています。また、同時実行されるセッションの管理に関する補助情報も提供されています。この更新により、ユーザーはセッションの制約を理解し、より効率的に作業を進めることができるようになります。全体として、ユーザーにとってスムーズで予測可能なセッション運用を促進し、作業効率を向上させることが目的です。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:768223a...MicrosoftDocs:ca0291a){target="_blank"}

# ハイライト
この差分では、「code-interpreter.md」ファイルにおいて、Code Interpreterセッションのタイムアウトに関する情報が追加され、セッション管理に関する内容が明確化されました。これにより、ユーザーはセッションがどのように制限されるかについてより良い理解が得られます。

## 新機能
- Code Interpreterセッションがデフォルトで1時間アクティブであることの記述。
- 30分間のアイドルタイムアウトが存在するという情報の追加。

## 破壊的変更
特に破壊的な変更はありませんでした。アップデートは主に情報の追加・明確化に留まっています。

## その他の更新
- 同時実行されるセッションについての詳細が追加され、ユーザーが同時に複数のセッションを管理する上での補助情報が提供されました。

# インサイト
この更新は、Code Interpreterのセッション管理に関する透明性を高めるためのものです。多くの場合、セッションが長時間にわたってアイドル状態に置かれると、予期しない切断が発生することがありますが、今回の変更によりユーザーはそのような状況を予測し、準備することができるでしょう。

デフォルトの1時間アクティブ状態と30分のアイドルタイムアウトは、リソースを効率的に管理するための重要な要素です。セッションの終了を防ぎ、必要な作業を継続するためには、ユーザーがこれらの制約を理解し計画を立てることが重要です。

さらに、同時に複数のセッションを実行する場合、一つのセッションがタイムアウトしたとしても、他のセッションは影響を受けないことが確認できます。これは、リソースの無駄遣いを防ぎながら、効率よく作業を進めたいユーザーにとってメリットとなります。

全体として、この改訂はユーザーにとって、よりスムーズで予測可能なセッションの運用を実現するためのものであり、結果として作業効率の向上につながるものと言えるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [code-interpreter.md](#item-95efbd) | minor update | コードインタープリタのセッションのタイムアウトに関する更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/openai/how-to/code-interpreter.md{#item-95efbd}

<details>
<summary>Diff</summary>
````diff
@@ -20,7 +20,7 @@ recommendations: false
 Code Interpreter allows the Assistants API to write and run Python code in a sandboxed execution environment. With Code Interpreter enabled, your Assistant can run code iteratively to solve more challenging code, math, and data analysis problems. When your Assistant writes code that fails to run, it can iterate on this code by modifying and running different code until the code execution succeeds.
 
 > [!IMPORTANT]
-> Code Interpreter has [additional charges](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) beyond the token based fees for Azure OpenAI usage. If your Assistant calls Code Interpreter simultaneously in two different threads, two code interpreter sessions are created. Each session is active by default for one hour.
+> Code Interpreter has [additional charges](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) beyond the token based fees for Azure OpenAI usage. If your Assistant calls Code Interpreter simultaneously in two different threads, two code interpreter sessions are created. Each session is active by default for 1 hour with an idle timeout of 30 minutes.
 
 ## Code interpreter support
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コードインタープリタのセッションのタイムアウトに関する更新"
}
```

### Explanation
この変更は、「code-interpreter.md」ファイルの内容に対する軽微な更新であり、Code Interpreterのセッションに関する重要な情報を明確にしました。具体的には、各セッションがデフォルトで1時間アクティブであることに加え、30分間のアイドルタイムアウトが設定されていることが追加されています。この情報は、ユーザーがリソースを効率的に管理する上で重要です。変更は、2つのコードインタープリタセッションが同時に作成されるという条件に関連しており、ユーザーに対し、同時実行中のセッションについての理解を助ける内容になっています。


